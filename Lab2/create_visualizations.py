#!/usr/bin/env python3
"""
Create simple visualizations for the Lab Assignment 2 report
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import os

# Set matplotlib to non-interactive backend
plt.switch_backend('Agg')

def create_research_questions_chart(metrics):
    """Create a bar chart for the three research questions results using dynamic metrics"""

    rq_data = {
        'RQ1\n(Developer\nPrecision)': round(metrics['developer_precision_rate'], 1),
        'RQ2\n(LLM\nGeneration)': round(metrics['llm_success_rate'], 1),
        'RQ3\n(Message\nRectification)': round(metrics['rectification_rate'], 1)
    }

    plt.figure(figsize=(10, 6))
    bars = plt.bar(rq_data.keys(), rq_data.values(),
                   color=['#e74c3c', '#2ecc71', '#3498db'], alpha=0.8)

    for bar, value in zip(bars, rq_data.values()):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{value}%', ha='center', va='bottom', fontweight='bold')

    plt.title('Research Questions Evaluation Results', fontsize=16, fontweight='bold')
    plt.ylabel('Hit Rate (%)', fontsize=12)
    plt.ylim(0, 110)
    plt.grid(axis='y', alpha=0.3)

    plt.text(0.5, 0.95, 'Higher percentages indicate better performance',
             transform=plt.gca().transAxes, ha='center', va='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig('research_questions_results.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: research_questions_results.png")

def create_keyword_frequency_chart(metrics):
    """Create a chart showing bug-fixing keyword frequencies from dynamic analysis"""

    kw_items = list(metrics['top_keywords'].items())
    keywords = [k for k, _ in kw_items]
    frequencies = [v for _, v in kw_items]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(keywords, frequencies, color='#9b59b6', alpha=0.8)

    for bar, freq in zip(bars, frequencies):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(frequencies)*0.02,
                 str(freq), ha='center', va='bottom', fontweight='bold')

    plt.title('Top Bug-Fixing Keywords in Commit Messages', fontsize=16, fontweight='bold')
    plt.xlabel('Keywords', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('keyword_frequency.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: keyword_frequency.png")

def create_file_types_chart(metrics):
    """Create a pie chart for file types distribution (top 5 + others)"""

    top_ft = metrics['top_file_types']  # dict already top 5
    total = metrics['total_file_entries']
    # Determine others count (total minus sum top5)
    top_sum = sum(top_ft.values())
    others = total - top_sum
    file_types = [f'.{k}' if k not in ['no_extension'] else 'no_extension' for k in top_ft.keys()]
    counts = list(top_ft.values())
    if others > 0:
        file_types.append('others')
        counts.append(others)
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#95a5a6'][:len(counts)]

    plt.figure(figsize=(10, 8))
    wedges, texts, autotexts = plt.pie(counts, labels=file_types, colors=colors,
                                       autopct='%1.1f%%', startangle=90)

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    plt.title('Distribution of File Types in Bug Fixes', fontsize=16, fontweight='bold')
    legend_labels = [f'{ft}: {count} files' for ft, count in zip(file_types, counts)]
    plt.legend(wedges, legend_labels, title="File Types", loc="center left",
               bbox_to_anchor=(1, 0, 0.5, 1))

    plt.tight_layout()
    plt.savefig('file_types_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: file_types_distribution.png")

def create_commit_analysis_chart(metrics):
    """Create a chart showing commit analysis breakdown using dynamic metrics"""

    categories = ['Total\nBug-fixing\nCommits', 'Merge\nCommits', 'Non-merge\nCommits']
    total = metrics['total_bug_commits']
    merges = metrics['merge_commits']
    non_merges = total - merges
    values = [total, merges, non_merges]
    colors = ['#34495e', '#e67e22', '#16a085']

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=colors, alpha=0.8)

    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (total * 0.01 + 5),
                 str(value), ha='center', va='bottom', fontweight='bold')

    plt.title('Bug-Fixing Commits Analysis', fontsize=16, fontweight='bold')
    plt.ylabel('Number of Commits', fontsize=12)
    plt.grid(axis='y', alpha=0.3)

    plt.text(0.5, 0.95, f"Average files per commit: {metrics['avg_files_per_commit']:.2f}",
             transform=plt.gca().transAxes, ha='center', va='top',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig('commit_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: commit_analysis.png")

def create_message_precision_breakdown(metrics):
    """Create a detailed breakdown of message precision dynamically"""

    categories = ['Precise\nMessages', 'Vague\nMessages', 'Neutral\nMessages']
    values = [metrics['precise_messages'], metrics['vague_messages'], metrics['neutral_messages']]
    total = sum(values)
    if total == 0:
        percentages = [0, 0, 0]
    else:
        percentages = [round(v / total * 100, 1) for v in values]
    colors = ['#2ecc71', '#e74c3c', '#95a5a6']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    bars = ax1.bar(categories, values, color=colors, alpha=0.8)
    for bar, value, pct in zip(bars, values, percentages):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.02 + 1,
                 f'{value}\n({pct}%)', ha='center', va='bottom', fontweight='bold')

    ax1.set_title('Developer Message Precision Breakdown', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Number of Messages', fontsize=12)
    ax1.grid(axis='y', alpha=0.3)

    wedges, texts, autotexts = ax2.pie(values, labels=categories, colors=colors,
                                       autopct='%1.1f%%', startangle=90)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    ax2.set_title('Message Precision Distribution', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('message_precision_breakdown.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: message_precision_breakdown.png")

def create_rectification_breakdown(metrics):
    """Create bar + pie charts for RQ3 (message rectification)"""
    improved = metrics.get('improvement_count', 0)
    valid = metrics.get('valid_rectifications', 0) - improved
    empty = metrics.get('total_rectifications', 0) - metrics.get('valid_rectifications', 0)
    # Ensure non-negative
    valid = max(valid, 0)
    empty = max(empty, 0)
    categories = ['Improved', 'Valid (No Major Change)', 'Empty/Invalid']
    values = [improved, valid, empty]
    total = sum(values) if sum(values) else 1
    percentages = [v/total*100 for v in values]
    colors = ['#27ae60', '#f1c40f', '#c0392b']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    bars = ax1.bar(categories, values, color=colors, alpha=0.85)
    for bar, value, pct in zip(bars, values, percentages):
        ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+max(values)*0.03 + 0.5,
                 f"{value}\n({pct:.1f}%)", ha='center', va='bottom', fontweight='bold')
    ax1.set_title('RQ3: Rectified Message Categories', fontweight='bold')
    ax1.set_ylabel('Count')
    ax1.grid(axis='y', alpha=0.3)

    wedges, texts, autotexts = ax2.pie(values, labels=categories, colors=colors,
                                       autopct='%1.1f%%', startangle=90)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    ax2.set_title('RQ3: Rectification Distribution', fontweight='bold')

    plt.suptitle('RQ3 - Commit Message Rectification Breakdown', fontweight='bold')
    plt.tight_layout()
    plt.savefig('rectification_breakdown.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: rectification_breakdown.png")

def create_summary_dashboard(metrics):
    """Create a comprehensive summary dashboard using dynamic metrics"""

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1. Research Questions Results
    rq_data = {
        'RQ1': round(metrics['developer_precision_rate'], 1),
        'RQ2': round(metrics['llm_success_rate'], 1),
        'RQ3': round(metrics['rectification_rate'], 1)
    }
    bars1 = ax1.bar(rq_data.keys(), rq_data.values(),
                    color=['#e74c3c', '#2ecc71', '#3498db'], alpha=0.8)
    for bar, value in zip(bars1, rq_data.values()):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{value}%', ha='center', va='bottom', fontweight='bold')
    ax1.set_title('Research Questions Results', fontweight='bold')
    ax1.set_ylabel('Hit Rate (%)')
    ax1.set_ylim(0, 110)
    ax1.grid(axis='y', alpha=0.3)

    # 2. Top Keywords
    kw_items = list(metrics['top_keywords'].items())
    keywords = [k for k, _ in kw_items]
    frequencies = [v for _, v in kw_items]
    ax2.bar(keywords, frequencies, color='#9b59b6', alpha=0.8)
    ax2.set_title('Top Bug-Fixing Keywords', fontweight='bold')
    ax2.set_ylabel('Frequency')
    ax2.tick_params(axis='x', rotation=45)

    # 3. File Types (top 5)
    ft_items = list(metrics['top_file_types'].items())
    file_types = [f'.{k}' if k not in ['no_extension'] else 'no_ext' for k, _ in ft_items]
    counts = [v for _, v in ft_items]
    ax3.bar(file_types, counts, color='#f39c12', alpha=0.8)
    ax3.set_title('Top File Types in Bug Fixes', fontweight='bold')
    ax3.set_ylabel('Number of Files')

    # 4. Commit Types
    commit_types = ['Total', 'Merge', 'Non-merge']
    commit_counts = [metrics['total_bug_commits'], metrics['merge_commits'], metrics['total_bug_commits'] - metrics['merge_commits']]
    ax4.bar(commit_types, commit_counts,
            color=['#34495e', '#e67e22', '#16a085'], alpha=0.8)
    ax4.set_title('Commit Types Analysis', fontweight='bold')
    ax4.set_ylabel('Number of Commits')

    plt.suptitle('Lab Assignment 2 - Flask Repository Analysis Dashboard',
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('analysis_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: analysis_dashboard.png")

def compute_metrics():
    """Compute all dynamic metrics replicating logic from quick_analysis.py"""
    metrics = {}
    try:
        bug_commits = pd.read_csv('bug_fixing_commits.csv')
        predictions = pd.read_csv('commit_predictions.csv')
    except Exception as e:
        print(f"❌ Failed to load CSVs for metrics: {e}")
        return None

    # Commit counts
    total_commits = len(bug_commits)
    merge_commits = bug_commits['Is a merge commit?'].sum() if 'Is a merge commit?' in bug_commits.columns else 0
    metrics['total_bug_commits'] = int(total_commits)
    metrics['merge_commits'] = int(merge_commits)

    # Files per commit
    files_per_commit = []
    if 'List of modified files' in bug_commits.columns:
        for files_str in bug_commits['List of modified files']:
            try:
                files_list = eval(files_str) if pd.notna(files_str) else []  # nosec - controlled educational context
                files_per_commit.append(len(files_list))
            except Exception:
                files_per_commit.append(0)
    metrics['avg_files_per_commit'] = float(np.mean(files_per_commit)) if files_per_commit else 0.0

    # Keyword counts
    keywords = ["fix", "bug", "fixes", "fixed", "crash", "issue", "error", "problem", "broken"]
    keyword_counts = {}
    if 'Message' in bug_commits.columns:
        for keyword in keywords:
            cnt = bug_commits['Message'].str.lower().str.contains(keyword, na=False).sum()
            keyword_counts[keyword] = int(cnt)
    top_keywords = dict(sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:5])
    metrics['top_keywords'] = top_keywords

    # Developer precision breakdown
    precise_indicators = ['fix', 'bug', 'error', 'issue', 'problem', 'crash', 'broken']
    vague_indicators = ['update', 'change', 'modify', 'refactor', 'cleanup']
    precise = vague = neutral = 0
    original_messages = predictions['Commit Message'].tolist() if 'Commit Message' in predictions.columns else []
    for msg in original_messages:
        if pd.isna(msg):
            neutral += 1
            continue
        msg_l = str(msg).lower()
        if any(x in msg_l for x in precise_indicators):
            precise += 1
        elif any(x in msg_l for x in vague_indicators):
            vague += 1
        else:
            neutral += 1
    total_messages = len(original_messages) if original_messages else 1
    metrics['precise_messages'] = precise
    metrics['vague_messages'] = vague
    metrics['neutral_messages'] = neutral
    metrics['developer_precision_rate'] = precise / total_messages * 100

    # LLM success rate
    llm_preds = predictions['LLM Inference (fix type)'].tolist() if 'LLM Inference (fix type)' in predictions.columns else []
    if llm_preds:
        meaningful = sum(0 if (pd.isna(p) or str(p).strip() in ['', 'nan']) else 1 for p in llm_preds)
        metrics['llm_success_rate'] = meaningful / len(llm_preds) * 100
    else:
        metrics['llm_success_rate'] = 0.0

    # Rectification rate
    rectified = predictions['Rectified Message'].tolist() if 'Rectified Message' in predictions.columns else []
    improvement = 0
    valid_rectifications = 0
    if rectified:
        for orig, rect in zip(original_messages, rectified):
            if pd.notna(rect) and str(rect).strip() not in ['', 'nan']:
                valid_rectifications += 1
                try:
                    if len(str(rect).strip()) > len(str(orig).strip()) * 0.8:
                        improvement += 1
                except Exception:
                    continue
        metrics['rectification_rate'] = improvement / len(rectified) * 100
    else:
        metrics['rectification_rate'] = 0.0
    metrics['improvement_count'] = improvement
    metrics['valid_rectifications'] = valid_rectifications
    metrics['total_rectifications'] = len(rectified)

    # File type counts from predictions 'File Name'
    file_extensions = []
    if 'File Name' in predictions.columns:
        for filename in predictions['File Name']:
            if pd.notna(filename) and '.' in str(filename):
                ext = str(filename).split('.')[-1].lower()
                file_extensions.append(ext)
            else:
                file_extensions.append('no_extension')
    ext_counts = Counter(file_extensions)
    metrics['top_file_types'] = dict(ext_counts.most_common(5))
    metrics['total_file_entries'] = len(file_extensions)

    return metrics

def main():
    """Create all visualizations with dynamic metrics"""
    print("Creating visualizations for Lab Assignment 2 (dynamic metrics)...")
    print("="*50)

    metrics = compute_metrics()
    if not metrics:
        print("❌ Aborting visualization creation due to missing metrics.")
        return

    try:
        create_research_questions_chart(metrics)
        create_keyword_frequency_chart(metrics)
        create_file_types_chart(metrics)
        create_commit_analysis_chart(metrics)
        create_message_precision_breakdown(metrics)
        create_rectification_breakdown(metrics)
        create_summary_dashboard(metrics)

        print("\n" + "="*50)
        print("ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
        print("="*50)
        print("Generated files:")
        print("• research_questions_results.png")
        print("• keyword_frequency.png")
        print("• file_types_distribution.png")
        print("• commit_analysis.png")
        print("• message_precision_breakdown.png")
        print("• rectification_breakdown.png")
        print("• analysis_dashboard.png")
        print("\nThese charts use the latest data from bug_fixing_commits.csv & commit_predictions.csv")

    except Exception as e:
        print(f"❌ Error creating visualizations: {e}")

if __name__ == "__main__":
    main()
