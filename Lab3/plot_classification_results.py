import pandas as pd
import matplotlib.pyplot as plt

def plot_classification_results(csv_path='final_lab3_results.csv'):
    df = pd.read_csv(csv_path)
    # Semantic_class distribution
    sem_counts = df['Semantic_class'].value_counts()
    plt.figure(figsize=(5,4))
    bars = plt.bar(sem_counts.index, sem_counts.values, color=['#4daf4a','#e41a1c'], edgecolor='black')
    plt.title('Semantic Class Distribution')
    plt.xlabel('Semantic Class')
    plt.ylabel('Count')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, str(int(yval)), ha='center', va='bottom', fontsize=12)
    plt.tight_layout()
    plt.savefig('semantic_class_distribution.png')
    plt.close()

    # Token_class distribution
    tok_counts = df['Token_class'].value_counts()
    plt.figure(figsize=(5,4))
    bars = plt.bar(tok_counts.index, tok_counts.values, color=['#377eb8','#ff7f00'], edgecolor='black')
    plt.title('Token Class Distribution')
    plt.xlabel('Token Class')
    plt.ylabel('Count')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, str(int(yval)), ha='center', va='bottom', fontsize=12)
    plt.tight_layout()
    plt.savefig('token_class_distribution.png')
    plt.close()

    # Classes_Agree distribution (bar chart)
    agree_counts = df['Classes_Agree'].value_counts()
    plt.figure(figsize=(5,4))
    bars = plt.bar(agree_counts.index, agree_counts.values, color=['#984ea3','#a65628'], edgecolor='black')
    plt.title('Semantic vs Token Class Agreement')
    plt.xlabel('Agreement')
    plt.ylabel('Count')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, str(int(yval)), ha='center', va='bottom', fontsize=12)
    plt.tight_layout()
    plt.savefig('class_agreement_distribution.png')
    plt.close()
    # Classes_Agree distribution (pie chart)
    plt.figure(figsize=(5,5))
    plt.pie(agree_counts.values, labels=agree_counts.index, autopct='%1.1f%%', colors=['#984ea3','#a65628'], startangle=90, counterclock=False)
    plt.title('Class Agreement Distribution (Pie Chart)')
    plt.tight_layout()
    plt.savefig('class_agreement_pie.png')
    plt.close()

    # Optional: Grouped bar for agreement breakdown
    grouped = df.groupby(['Semantic_class','Token_class'])['Classes_Agree'].value_counts().unstack(fill_value=0)
    grouped.plot(kind='bar', stacked=True, color=['#66c2a5','#fc8d62'], figsize=(7,5), edgecolor='black')
    plt.title('Agreement Breakdown by Semantic and Token Class')
    plt.xlabel('Semantic / Token Class')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('agreement_breakdown.png')
    plt.close()

    # 2x2 matrix (heatmap) for Semantic_class vs Token_class
    import numpy as np
    import seaborn as sns
    matrix = df.groupby(['Semantic_class','Token_class']).size().unstack(fill_value=0)
    plt.figure(figsize=(5,4))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Semantic vs Token Class (2x2 Matrix)')
    plt.xlabel('Token Class')
    plt.ylabel('Semantic Class')
    plt.tight_layout()
    plt.savefig('semantic_token_matrix.png')
    plt.close()

if __name__ == '__main__':
    plot_classification_results()
