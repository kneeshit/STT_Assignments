import csv
import os
import argparse
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from datetime import datetime

# Path to the consolidated CSV file
# List of CSV files to process
DEFAULT_CSVS = [
    "consolidated_commit_diffs.csv"  # Add more CSV file paths here if needed
]

def get_file_type_from_commit_msg(commit_msg):
    msg = commit_msg.lower()
    if "readme" in msg:
        return "README"
    if "license" in msg:
        return "LICENSE"
    if "test" in msg:
        return "Test Code"
    return "Source Code"


repo_filetype_mismatches = {}
# mismatch_counts counts NON-identical algorithm outputs (Discrepancy == "No")
mismatch_counts = Counter({"Source Code": 0, "Test Code": 0, "README": 0, "LICENSE": 0})
yesno_counts = Counter({"Yes": 0, "No": 0})  # Yes = identical diffs, No = different
filetype_yesno = {ft: Counter({"Yes": 0, "No": 0}) for ft in mismatch_counts.keys()}

# Additional aggregations
repo_level = defaultdict(lambda: Counter({"identical": 0, "different": 0}))
filetype_repo_mismatches = defaultdict(lambda: Counter({"Source Code": 0, "Test Code": 0, "README": 0, "LICENSE": 0}))

# Diff size statistics (sampled)
diff_sizes = {
    "myers_chars": [],
    "hist_chars": [],
    "myers_lines": [],
    "hist_lines": []
}

def _read_text(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read()
    except Exception:
        return ""

def analyze_mismatches(csv_paths, sample_diff_sizes=True, diff_sample_limit=5000):
    total_rows = 0
    for csv_path in csv_paths:
        if not os.path.exists(csv_path):
            print(f"Warning: {csv_path} not found.")
            continue
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                total_rows += 1
                discrepancy = row.get("Discrepancy", "")
                if discrepancy not in ("Yes", "No"):
                    continue
                yesno_counts[discrepancy] += 1
                repo = os.path.basename(row.get("repo_path", "")) or "(unknown)"
                file_type = get_file_type_from_commit_msg(row.get("commit_message", ""))

                # Repo-level outcome counts
                if discrepancy == "Yes":
                    repo_level[repo]["identical"] += 1
                else:
                    repo_level[repo]["different"] += 1

                if file_type in mismatch_counts:
                    if discrepancy == "No":
                        mismatch_counts[file_type] += 1
                        if repo not in repo_filetype_mismatches:
                            repo_filetype_mismatches[repo] = Counter({"Source Code": 0, "Test Code": 0, "README": 0, "LICENSE": 0})
                        repo_filetype_mismatches[repo][file_type] += 1
                        filetype_repo_mismatches[repo][file_type] += 1
                    filetype_yesno[file_type][discrepancy] += 1

                # Diff size sampling
                if sample_diff_sizes and len(diff_sizes["myers_chars"]) < diff_sample_limit:
                    myers_path = row.get("diff_myers1_path", "")
                    hist_path = row.get("diff_hist2_path", "")
                    if myers_path and os.path.exists(myers_path):
                        content = _read_text(myers_path)
                        diff_sizes["myers_chars"].append(len(content))
                        diff_sizes["myers_lines"].append(content.count('\n') + (1 if content else 0))
                    if hist_path and os.path.exists(hist_path):
                        content = _read_text(hist_path)
                        diff_sizes["hist_chars"].append(len(content))
                        diff_sizes["hist_lines"].append(content.count('\n') + (1 if content else 0))
    return total_rows

def plot_stats(show=False):
    labels = list(mismatch_counts.keys())
    values = [mismatch_counts[label] for label in labels]
    plt.figure(figsize=(8,5))
    plt.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
    plt.title("#Mismatches by File Type")
    plt.ylabel("Count of Mismatches")
    plt.xlabel("File Type")
    for i, v in enumerate(values):
        plt.text(i, v + 0.2, str(v), ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig("mismatch_stats.png")
    if show:
        plt.show()
    else:
        plt.close()

def plot_yesno_pie(show=False):
    plt.figure(figsize=(6,6))
    plt.pie([yesno_counts["Yes"], yesno_counts["No"]], labels=["Identical (Yes)", "Different (No)"], autopct='%1.1f%%', colors=["#4CAF50", "#F44336"])
    plt.title("Overall Diff Outcome Ratio")
    plt.savefig("yesno_pie.png")
    if show:
        plt.show()
    else:
        plt.close()

def plot_yesno_bar_by_filetype(show=False):
    labels = list(filetype_yesno.keys())
    yes_vals = [filetype_yesno[ft]["Yes"] for ft in labels]
    no_vals = [filetype_yesno[ft]["No"] for ft in labels]
    x = range(len(labels))
    plt.figure(figsize=(8,5))
    plt.bar(x, yes_vals, width=0.4, label="Identical", color="#4CAF50")
    plt.bar([i+0.4 for i in x], no_vals, width=0.4, label="Different", color="#F44336")
    plt.xticks([i+0.2 for i in x], labels)
    plt.xlabel("File Type")
    plt.ylabel("Count")
    plt.title("Discrepancy Yes/No by File Type")
    plt.legend()
    plt.tight_layout()
    plt.savefig("yesno_bar_by_filetype.png")
    if show:
        plt.show()
    else:
        plt.close()

def summarize(enable_diff_sizes=True):
    lines = []
    total = yesno_counts["Yes"] + yesno_counts["No"]
    if total == 0:
        lines.append("No data processed.")
        text = "\n".join(lines)
        print(text)
        return text
    ident_pct = 100 * yesno_counts["Yes"] / total
    diff_pct = 100 * yesno_counts["No"] / total
    lines.append("=== Diff Algorithm Outcome Summary ===")
    lines.append(f"Total file-level change rows: {total}")
    lines.append(f"Identical (Myers == Histogram): {yesno_counts['Yes']} ({ident_pct:.2f}%)")
    lines.append(f"Different  (Myers != Histogram): {yesno_counts['No']} ({diff_pct:.2f}%)")
    lines.append("")
    lines.append("-- Mismatch Counts by File Type -- (Discrepancy == 'No')")
    for ft in mismatch_counts:
        ft_total = filetype_yesno[ft]["Yes"] + filetype_yesno[ft]["No"]
        rate = 100 * mismatch_counts[ft] / ft_total if ft_total else 0
        lines.append(f"{ft}: {mismatch_counts[ft]} mismatches ({rate:.2f}% of its rows)")
    if repo_level:
        lines.append("")
        lines.append("-- Per Repository Outcome --")
        for repo, counts in sorted(repo_level.items()):
            r_total = counts['identical'] + counts['different']
            i_rate = 100 * counts['identical'] / r_total if r_total else 0
            d_rate = 100 * counts['different'] / r_total if r_total else 0
            lines.append(f"{repo}: identical={counts['identical']} ({i_rate:.2f}%), different={counts['different']} ({d_rate:.2f}%)")
    if repo_filetype_mismatches:
        lines.append("")
        lines.append("-- Mismatches by File Type per Repo --")
        lines.append("Repo\tSource Code\tTest Code\tREADME\tLICENSE")
        for repo, counts in repo_filetype_mismatches.items():
            lines.append(f"{repo}\t{counts['Source Code']}\t{counts['Test Code']}\t{counts['README']}\t{counts['LICENSE']}")

    if enable_diff_sizes and diff_sizes['myers_chars'] and diff_sizes['hist_chars']:
        import statistics
        def stats(arr):
            if len(arr) == 1:
                return {'count': 1, 'mean': arr[0], 'median': arr[0], 'p95': arr[0]}
            return {
                'count': len(arr),
                'mean': statistics.mean(arr),
                'median': statistics.median(arr),
                'p95': statistics.quantiles(arr, n=20)[18]
            }
        mc = stats(diff_sizes['myers_chars']); hc = stats(diff_sizes['hist_chars'])
        ml = stats(diff_sizes['myers_lines']); hl = stats(diff_sizes['hist_lines'])
        lines.append("")
        lines.append("-- Diff Size Stats (Characters) --")
        lines.append(f"Myers: mean={mc['mean']:.1f} median={mc['median']:.1f} p95={mc['p95']:.1f} n={mc['count']}")
        lines.append(f"Hist:  mean={hc['mean']:.1f} median={hc['median']:.1f} p95={hc['p95']:.1f} n={hc['count']}")
        lines.append("-- Diff Size Stats (Lines) --")
        lines.append(f"Myers: mean={ml['mean']:.1f} median={ml['median']:.1f} p95={ml['p95']:.1f}")
        lines.append(f"Hist:  mean={hl['mean']:.1f} median={hl['median']:.1f} p95={hl['p95']:.1f}")

    lines.append("")
    lines.append(f"Generated: {datetime.utcnow().isoformat()}Z")
    summary = "\n".join(lines)
    print(summary)
    with open("stats_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    return summary

def plot_repo_filetype_mismatches(show=False):
    if not repo_filetype_mismatches:
        return
    try:
        import numpy as np
    except ImportError:
        print("NumPy not installed; skipping repo filetype mismatch plot.")
        return
    repos = list(repo_filetype_mismatches.keys())
    file_types = ["Source Code", "Test Code", "README", "LICENSE"]
    data = np.array([[repo_filetype_mismatches[repo][ft] for ft in file_types] for repo in repos])
    x = np.arange(len(repos))
    width = 0.2
    plt.figure(figsize=(10,6))
    for i, ft in enumerate(file_types):
        plt.bar(x + i*width, data[:,i], width, label=ft)
    plt.xticks(x + width*1.5, repos, rotation=20, ha='right')
    plt.xlabel("Repository")
    plt.ylabel("Mismatch Count (Non-identical Diff Pairs)")
    plt.title("Mismatch Count of File Types per Repository")
    plt.legend()
    plt.tight_layout()
    plt.savefig("repo_filetype_mismatches.png")
    if show:
        plt.show()
    else:
        plt.close()

def parse_args():
    p = argparse.ArgumentParser(description="Analyze diff algorithm outcome statistics.")
    p.add_argument('--csv', nargs='*', default=DEFAULT_CSVS, help='One or more consolidated CSV file paths.')
    p.add_argument('--no-diff-size', action='store_true', help='Disable diff size sampling and stats.')
    p.add_argument('--limit-samples', type=int, default=5000, help='Max diff samples for size stats.')
    p.add_argument('--show', action='store_true', help='Show plots interactively.')
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    total_rows = analyze_mismatches(args.csv, sample_diff_sizes=not args.no_diff_size, diff_sample_limit=args.limit_samples)
    print(f"Processed rows: {total_rows}")
    plot_stats(show=args.show)
    plot_yesno_pie(show=args.show)
    plot_yesno_bar_by_filetype(show=args.show)
    plot_repo_filetype_mismatches(show=args.show)
    summarize(enable_diff_sizes=not args.no_diff_size)
