import os
from radon.metrics import mi_visit
from radon.complexity import cc_visit
from radon.raw import analyze
from load_data import load_commit_dataset, get_code_pair, get_diff_content
import pandas as pd

def compute_metrics(code):
    try:
        mi = mi_visit(code, True) if code else None
        cc = sum([block.complexity for block in cc_visit(code)]) if code else None
        loc = analyze(code).loc if code else None
        return mi, cc, loc
    except SyntaxError:
        return None, None, None

def main():
    import pandas as pd
    file_df = pd.read_csv('../Lab2/commit_predictions.csv')
    results = []
    for idx, row in file_df.iterrows():
        filename = row['File Name']
        if not filename or not filename.endswith('.py'):
            continue  # Skip non-Python files
        commit_hash = row['Commit Hash']
        code_before_path = row['Source Code Before File Path']
        code_after_path = row['Source Code After File Path']
        code_before = open(code_before_path, encoding='utf-8').read() if code_before_path and os.path.exists(code_before_path) else None
        code_after = open(code_after_path, encoding='utf-8').read() if code_after_path and os.path.exists(code_after_path) else None
        mi_b, cc_b, loc_b = compute_metrics(code_before)
        mi_a, cc_a, loc_a = compute_metrics(code_after)
        results.append({
            'Commit Hash': commit_hash,
            'File Name': filename,
            'MI_Before': mi_b,
            'MI_After': mi_a,
            'MI_Change': (mi_a - mi_b) if mi_a and mi_b else None,
            'CC_Before': cc_b,
            'CC_After': cc_a,
            'CC_Change': (cc_a - cc_b) if cc_a and cc_b else None,
            'LOC_Before': loc_b,
            'LOC_After': loc_a,
            'LOC_Change': (loc_a - loc_b) if loc_a and loc_b else None
        })
    metrics_df = pd.DataFrame(results)
    metrics_df.to_csv('structural_metrics_results.csv', index=False)
    print('Structural metrics saved to structural_metrics_results.csv')

if __name__ == '__main__':
    main()
