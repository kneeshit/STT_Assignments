import pandas as pd
from collections import Counter
from load_data import load_commit_dataset, get_diff_content
import matplotlib.pyplot as plt

def main():    
    # Commit-level stats
    commit_df = pd.read_csv('../Lab2/bug_fixing_commits.csv')
    total_commits = len(commit_df)
    all_files = []
    files_per_commit = []
    for files in commit_df['List of modified files']:
        if isinstance(files, str):
            try:
                file_list = eval(files)
            except Exception:
                file_list = [files]
            all_files.extend(file_list)
            files_per_commit.append(len(file_list))
        else:
            files_per_commit.append(0)
    total_files = len(all_files)
    avg_files_per_commit = total_files / total_commits if total_commits else 0
    # Print summary stats
    print(f"Total commits: {total_commits}")
    print(f"Total files: {total_files}")
    print(f"Average files per commit: {avg_files_per_commit:.2f}")

    # Visual summary stats as a bar chart
    stats_names = ['Total Commits', 'Total Files', 'Avg Files/Commit']
    stats_values = [total_commits, total_files, avg_files_per_commit]
    plt.figure(figsize=(7,4))
    bars = plt.bar(stats_names, stats_values, color=['blue','orange','green'], edgecolor='black')
    plt.title('Summary Statistics')
    plt.ylabel('Count / Value')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + max(stats_values)*0.01, f'{yval:.2f}', ha='center', va='bottom', fontsize=12)
    plt.tight_layout()
    plt.savefig('summary_stats.png')
    plt.close()
    # print(f"Total commits: {total_commits}")
    # print(f"Total files: {total_files}")
    # print(f"Average files per commit: {avg_files_per_commit:.2f}")
    # Plot: Distribution of files per commit
    plt.figure(figsize=(8,5))
    n, bins, patches = plt.hist(files_per_commit, bins=range(1, max(files_per_commit)+2), color='skyblue', edgecolor='black')
    plt.title('Distribution of Number of Files per Commit')
    plt.xlabel('Files per Commit')
    plt.ylabel('Number of Commits')
    # Add value labels
    for i in range(len(n)):
        plt.text(bins[i]+0.5, n[i], str(int(n[i])), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('files_per_commit_distribution.png')
    plt.close()
    # File-level stats
    file_df = pd.read_csv('../Lab2/commit_predictions.csv')
    extensions = [f.split('.')[-1] for f in file_df['File Name'] if f and '.' in f]
    ext_counter = Counter(extensions)
    most_common_ext = ext_counter.most_common(8)
    # Plot: Top 8 file extensions
    if most_common_ext:
        ext_names, ext_counts = zip(*most_common_ext)
        plt.figure(figsize=(8,4))
        bars = plt.bar(ext_names, ext_counts, color='orange', edgecolor='black')
        plt.title('Top 8 Most Common File Extensions')
        plt.xlabel('File Extension')
        plt.ylabel('Count')
        # Add value labels
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, str(int(yval)), ha='center', va='bottom', fontsize=10)
        plt.tight_layout()
        plt.savefig('top8_file_extensions.png')
        plt.close()
    # Plot: Top 8 most frequently modified filenames
    filename_counter = Counter(file_df['File Name'])
    most_common_files = filename_counter.most_common(8)
    if most_common_files:
        file_names, file_counts = zip(*most_common_files)
        plt.figure(figsize=(10,4))
        bars = plt.barh(file_names, file_counts, color='purple', edgecolor='black')
        plt.title('Top 8 Most Frequently Modified Filenames')
        plt.xlabel('Count')
        plt.ylabel('Filename')
        # Add value labels
        for bar in bars:
            xval = bar.get_width()
            plt.text(xval, bar.get_y() + bar.get_height()/2, str(int(xval)), ha='left', va='center', fontsize=10)
        plt.tight_layout()
        plt.savefig('top8_filenames.png')
        plt.close()
    if 'LLM Inference (fix type)' in file_df.columns:
        # Filter out non-string fix types
        fix_types_raw = file_df['LLM Inference (fix type)']
        fix_types_filtered = [ft for ft in fix_types_raw if isinstance(ft, str)]
        fix_type_counter = Counter(fix_types_filtered)
    # print(f"Fix type distribution: {fix_type_counter}")
        if fix_type_counter:
            # Show only top 8 fix types for readability
            top_fix_types = fix_type_counter.most_common(8)
            fix_types, fix_counts = zip(*top_fix_types)
            plt.figure(figsize=(10,5))
            bars = plt.barh(fix_types, fix_counts, color='green', edgecolor='black')
            plt.title('Top 8 Most Common Fix Types')
            plt.xlabel('Count')
            plt.ylabel('Fix Type')
            # Add value labels
            for bar in bars:
                xval = bar.get_width()
                plt.text(xval, bar.get_y() + bar.get_height()/2, str(int(xval)), ha='left', va='center', fontsize=10)
            plt.tight_layout()
            plt.savefig('top8_fix_types.png')
            plt.close()
    else:
        pass  # print("LLM Inference (fix type) column not found in commit_predictions.csv.")

if __name__ == '__main__':
    main()
