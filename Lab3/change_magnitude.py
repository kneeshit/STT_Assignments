import os
import pandas as pd
from load_data import load_commit_dataset, get_code_pair, get_diff_content
from transformers import AutoTokenizer, AutoModel
import torch
import sacrebleu

def semantic_similarity(code1, code2, tokenizer, model):
    if not code1 or not code2:
        return None
    inputs1 = tokenizer(code1, return_tensors="pt", truncation=True, max_length=512)
    inputs2 = tokenizer(code2, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        emb1 = model(**inputs1).last_hidden_state.mean(dim=1)
        emb2 = model(**inputs2).last_hidden_state.mean(dim=1)
    sim = torch.nn.functional.cosine_similarity(emb1, emb2).item()
    return sim

def token_similarity(code1, code2):
    if not code1 or not code2:
        return None
    bleu = sacrebleu.corpus_bleu([code2], [[code1]])
    return bleu.score / 100.0  # Normalize to 0-1

def main():
    import pandas as pd
    file_df = pd.read_csv('../Lab2/commit_predictions.csv')
    tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
    model = AutoModel.from_pretrained("microsoft/codebert-base")
    results = []
    for idx, row in file_df.iterrows():
        commit_hash = row['Commit Hash']
        filename = row['File Name']
        code_before_path = row['Source Code Before File Path']
        code_after_path = row['Source Code After File Path']
        code_before = open(code_before_path, encoding='utf-8').read() if code_before_path and os.path.exists(code_before_path) else None
        code_after = open(code_after_path, encoding='utf-8').read() if code_after_path and os.path.exists(code_after_path) else None
        sem_sim = semantic_similarity(code_before, code_after, tokenizer, model)
        tok_sim = token_similarity(code_before, code_after)
        results.append({
            'Commit Hash': commit_hash,
            'File Name': filename,
            'Semantic_Similarity': sem_sim,
            'Token_Similarity': tok_sim
        })
    sim_df = pd.DataFrame(results)
    sim_df.to_csv('change_magnitude_results.csv', index=False)
    print('Change magnitude metrics saved to change_magnitude_results.csv')

if __name__ == '__main__':
    main()
