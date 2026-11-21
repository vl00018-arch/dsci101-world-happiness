import pandas as pd
from data_loader import load_data

years, dfs = load_data()

pairs = [
    ("Score", "Generosity"),
    ("Freedom", "Generosity"),
    ("GDP", "Corruption"),
    ("GDP", "Freedom")
]

results = []

for y in years:
    df = dfs[y]
    for col1, col2 in pairs:
        pearson_val = df[col1].corr(df[col2], method="pearson")
        spearman_val = df[col1].corr(df[col2], method="spearman")
        kendall_val = df[col1].corr(df[col2], method="kendall")
        
        results.append({
            "Year": y,
            "Pair": f"{col1} vs {col2}",
            "Pearson": round(pearson_val, 4),
            "Spearman": round(spearman_val, 4),
            "Kendall": round(kendall_val, 4)
        })

results_df = pd.DataFrame(results)

print("=" * 75)
print("TASK 6: PEARSON, SPEARMAN, AND KENDALL CORRELATIONS (2015–2019)")
print("=" * 75)
print(results_df.to_string(index=False))

# Optional: Save the table to plots/ or your folder for easy reference
results_df.to_csv("plots/task6_correlations.csv", index=False)
print("\nSaved correlation table to 'plots/task6_correlations.csv'!")