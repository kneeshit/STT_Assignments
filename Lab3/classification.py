import pandas as pd
from load_data import get_diff_content

def classify_row(row):
    sem = row['Semantic_Similarity']
    tok = row['Token_Similarity']
    sem_class = 'Minor' if sem is not None and sem >= 0.9 else 'Major'
    tok_class = 'Minor' if tok is not None and tok >= 0.9 else 'Major'
    agree = 'YES' if sem_class == tok_class else 'NO'
    return pd.Series({'Semantic_class': sem_class, 'Token_class': tok_class, 'Classes_Agree': agree})

def main():
    import pandas as pd
    struct_df = pd.read_csv('structural_metrics_results.csv')
    sim_df = pd.read_csv('change_magnitude_results.csv')
    # Merge on Commit Hash and File Name
    merged = pd.merge(struct_df, sim_df, on=['Commit Hash', 'File Name'], how='outer')
    # Classify
    class_df = merged.apply(classify_row, axis=1)
    final_df = pd.concat([merged, class_df], axis=1)
    final_df.to_csv('final_lab3_results.csv', index=False)
    print('Final results saved to final_lab3_results.csv')

if __name__ == '__main__':
    main()
