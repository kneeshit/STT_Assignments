# Automatic Comparison of Diff Algorithms: Myers vs Histogram

To automatically determine which diff algorithm performed better, follow these steps:

## 1. Define Evaluation Criteria
- **Discrepancy Rate:** Use the 'Discrepancy' column in your dataset. Fewer mismatches (Discrepancy == "No") may indicate better performance.
- **File Type Sensitivity:** Analyze performance per file type (Source Code, Test Code, README, LICENSE) to see if one algorithm excels in specific contexts.
- **Manual/Oracle Comparison (Optional):** If you have ground truth or expected diffs, compare algorithm outputs to this reference.

## 2. Implementation Steps
- **Count Mismatches:** For each algorithm, count the number of mismatches (cases where its output differs from the other or from ground truth).
- **Aggregate Statistics:** Summarize results by file type and overall.
- **Visualize Results:** Use bar plots or tables to compare algorithms.

## 3. Example Code Outline
```python
# Pseudocode for automatic comparison
import csv
myers_better = 0
hist_better = 0
with open('consolidated_commit_diffs.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # If you have ground truth, compare each diff to it
        # Otherwise, use discrepancy or other heuristics
        if row['Discrepancy'] == 'No':
            # Optionally, analyze which algorithm is closer to expected
            pass
        # Count and compare as needed
```

## 4. Decision
- The algorithm with fewer mismatches or better alignment with expected changes is considered superior for your dataset.
- You may also report results per file type for more nuanced insights.

## 5. Further Improvements
- Use more advanced metrics (e.g., diff size, semantic similarity).
- Incorporate user feedback or manual review for ambiguous cases.

---
**Summary:**
Automatically compare algorithms by counting mismatches and analyzing results by file type and overall. Use visualizations and, if available, ground truth data for more robust evaluation.
