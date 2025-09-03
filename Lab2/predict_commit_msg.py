import csv
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the pre-trained model and tokenizer
MODEL_NAME = "mamiksik/CommitPredictorT5"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def predict_fix_type(diff_text):
    # Prepare input for the model
    input_text = f"commit: {diff_text}"
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=32)
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return prediction

# Paths
csv_path = "commit_diffs.csv"
output_csv_path = "commit_predictions.csv"

diff_col_name = "Diff File Path"

with open(csv_path, "r", encoding="utf-8") as infile, open(output_csv_path, "w", newline='', encoding="utf-8") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["LLM Inference (fix type)"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in reader:
        diff_path = row.get(diff_col_name, "")
        fix_type = ""
        if diff_path and os.path.exists(diff_path):
            with open(diff_path, "r", encoding="utf-8") as diff_file:
                diff_text = diff_file.read()
                if diff_text.strip():
                    fix_type = predict_fix_type(diff_text)
        row["LLM Inference (fix type)"] = fix_type
        writer.writerow(row)

print(f"Predictions written to {output_csv_path}")
