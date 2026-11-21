import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data

years, dfs = load_data()

features = ["GDP", "Social_Support", "Health", "Freedom", "Generosity", "Corruption"]
corr_records = {}

print("=" * 65)
print("TASK 7: VARIABLES WITH STRONGEST RELATIONSHIP TO HAPPINESS SCORE")
print("=" * 65)

for y in years:
    # Calculate Pearson correlation with Score and sort from strongest to weakest
    corrs = dfs[y][["Score"] + features].corr()["Score"].drop("Score").sort_values(ascending=False)
    corr_records[y] = corrs
    
    print(f"\n--- Year {y} (Ranked Strongest to Weakest) ---")
    print(corrs.round(4).to_string())

# Combine into a summary table (Features x Years)
summary_df = pd.DataFrame(corr_records)
summary_df["Average_Correlation"] = summary_df.mean(axis=1)
summary_df = summary_df.sort_values(by="Average_Correlation", ascending=False)

print("\n" + "=" * 65)
print("SUMMARY ACROSS ALL YEARS (2015–2019)")
print("=" * 65)
print(summary_df.round(4).to_string())

# Save summary table and visualization for GitHub
summary_df.round(4).to_csv("plots/task7_strongest_predictors.csv")

plt.figure(figsize=(10, 6))
sns.heatmap(
    summary_df[years],
    annot=True,
    fmt=".3f",
    cmap="YlGnBu",
    cbar_kws={"label": "Correlation with Happiness Score"}
)
plt.title("Task 7 — Correlation with Happiness Score by Factor & Year (2015–2019)")
plt.xlabel("Year")
plt.ylabel("Factor")
plt.tight_layout()
plt.savefig("plots/task7_score_correlations_heatmap.png", dpi=150)
plt.close()

print("\nSaved table to 'plots/task7_strongest_predictors.csv' and heatmap to 'plots/task7_score_correlations_heatmap.png'!")
