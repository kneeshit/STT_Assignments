
import csv
import os
import subprocess
from pydriller import Repository


# List of repo paths to analyze
repo_paths = [			# Update with actual relative/absolute paths
	"butterknife",
	"alpine",        
	"ninja"         
]
output_csv = "consolidated_commit_diffs.csv"
codes_dir = "codes"
diffs_dir = "diffs"
limit = 1000
os.makedirs(codes_dir, exist_ok=True)
os.makedirs(diffs_dir, exist_ok=True)

def write_file(path, content):
	with open(path, 'w', encoding='utf-8') as f:
		f.write(content or "")

def get_diff(repo_path, parent_sha, sha, filepath, algorithm):
	cmd = [
		"git", "diff", "-w", "--ignore-blank-lines",
		f"--diff-algorithm={algorithm}",
		parent_sha, sha, "--", filepath
	]
	try:
		result = subprocess.run(cmd, cwd=repo_path, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
		return result.stdout
	except Exception:
		return ""

with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
	writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	writer.writerow([
		"repo_path",
		"old_file_path",
		"new_file_path",
		"commit_SHA",
		"parent_commit_SHA",
		"commit_message",
		"diff_myers1_path",
		"diff_hist2_path",
		"Discrepancy"
	])

	for repo_path in repo_paths:
		repo_limit = limit
		for commit in Repository(repo_path).traverse_commits():
			repo_limit -= 1
			if repo_limit < 0:
				break

			parent_sha = commit.parents[0] if commit.parents else ""
			for mod in commit.modified_files:
				before = mod.source_code_before or ""
				after = mod.source_code or ""
				base_filename = f"{os.path.basename(repo_path)}_{commit.hash}_{mod.filename}"
				# Sanitize filename for Windows
				for ch in [os.sep, '/', '\\', ':', '*', '?', '"', '<', '>', '|']:
					base_filename = base_filename.replace(ch, '_')
				before_filename = f"{base_filename}_before.txt"
				after_filename = f"{base_filename}_after.txt"
				myers_filename = f"{base_filename}_diff_myers.txt"
				hist_filename = f"{base_filename}_diff_hist.txt"
				before_path = os.path.join(codes_dir, before_filename)
				after_path = os.path.join(codes_dir, after_filename)
				myers_path = os.path.join(diffs_dir, myers_filename)
				hist_path = os.path.join(diffs_dir, hist_filename)
				write_file(before_path, before)
				write_file(after_path, after)

				rel_filepath = mod.new_path or mod.old_path or mod.filename
				diff_myers = get_diff(repo_path, parent_sha, commit.hash, rel_filepath, "myers")
				diff_hist = get_diff(repo_path, parent_sha, commit.hash, rel_filepath, "histogram")
				write_file(myers_path, diff_myers)
				write_file(hist_path, diff_hist)

				discrepancy = "Yes" if (diff_myers == diff_hist) else "No"

				writer.writerow([
					repo_path,
					before_path,
					after_path,
					commit.hash,
					parent_sha,
					commit.msg,
					myers_path,
					hist_path,
					discrepancy
				])
