import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

years, dfs = load_data()

# Create a 2x3 grid of subplots (6 panels total)
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
axes = axes.flatten()

# Panels 0 to 4: Individual scatter plots for 2015–2019
for i, y in enumerate(years):
    ax = axes[i]
    df = dfs[y]
    
    ax.scatter(df["GDP"], df["Health"], alpha=0.7, color="teal", edgecolors="white", s=45)
    
    # Label top 3 happiest, bottom 2 least happy, and every 25th country to avoid clutter
    highlight_idx = set([0, 1, 2, len(df) - 1, len(df) - 2] + list(range(0, len(df), 25)))
    for idx in highlight_idx:
        if idx < len(df):
            ax.annotate(
                df["Country"].iloc[idx],
                (df["GDP"].iloc[idx], df["Health"].iloc[idx]),
                fontsize=7.5,
                alpha=0.9
            )
            
    ax.set_title(str(y))
    ax.set_xlabel("GDP per Capita")
    ax.set_ylabel("Health (Life Expectancy)")
    ax.grid(True, linestyle="--", alpha=0.3)

# Panel 5 (Bottom-Right): All years combined comparison
ax_all = axes[5]
for y in years:
    ax_all.scatter(dfs[y]["GDP"], dfs[y]["Health"], alpha=0.5, s=25, label=str(y))

ax_all.set_title("All years (combined)")
ax_all.set_xlabel("GDP per Capita")
ax_all.set_ylabel("Health (Life Expectancy)")
ax_all.grid(True, linestyle="--", alpha=0.3)
ax_all.legend(fontsize=8)

# Main overall title and spacing adjustment
fig.suptitle("Task 2 — GDP per Capita vs. Health (Life Expectancy) by Year", fontsize=15)
plt.tight_layout()
plt.savefig("plots/task2_gdp_vs_health.png", dpi=150)
plt.close()

print("Combined Task 2 chart saved to 'plots/task2_gdp_vs_health.png'!")