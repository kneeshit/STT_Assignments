import os
import pandas as pd


LAB2_DIR = os.path.join(os.path.dirname(__file__), '..', 'Lab2')
CODES_DIR = os.path.join(LAB2_DIR, 'codes')

# Load commit-level dataset
def load_commit_dataset():
    path = os.path.join(LAB2_DIR, 'bug_fixing_commits.csv')
    return pd.read_csv(path)

# Load file-level dataset
def load_file_dataset():
    path = os.path.join(LAB2_DIR, 'commit_predictions.csv')
    return pd.read_csv(path)

# Utility to get before/after code for a given hash and filename

def get_code_pair(commit_hash, filename):
    # Normalize filename for codes folder
    base = os.path.basename(filename)
    # Remove extension for matching
    name, ext = os.path.splitext(base)
    # Compose file prefix
    prefix = f"{commit_hash}_{name}{ext}".replace('.', '').replace('-', '')
    before_path = os.path.join(CODES_DIR, f"{commit_hash}_{base}_before.txt")
    after_path = os.path.join(CODES_DIR, f"{commit_hash}_{base}_after.txt")
    code_before = open(before_path, encoding='utf-8').read() if os.path.exists(before_path) else None
    code_after = open(after_path, encoding='utf-8').read() if os.path.exists(after_path) else None
    return code_before, code_after

# Utility to read a diff file from a given path (relative or absolute)
def get_diff_content(diff_path):
    # If path is relative, assume it's relative to Lab2/diffs
    if not os.path.isabs(diff_path):
        base_dir = os.path.join(os.path.dirname(__file__), '..', 'Lab2', 'diffs')
        full_path = os.path.join(base_dir, diff_path)
    else:
        full_path = diff_path
    if os.path.exists(full_path):
        with open(full_path, encoding='utf-8') as f:
            return f.read()
    return None

# Example usage:
# df = load_commit_dataset()
# code_before, code_after = get_code_pair(df.iloc[0]['Hash'], 'flask.py')
