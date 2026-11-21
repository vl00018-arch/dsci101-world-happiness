import matplotlib.pyplot as plt
from data_loader import load_data

years, dfs = load_data()

# Create a 2x3 grid of subplots (6 panels total)
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()  # Flatten 2D grid into a 1D list of 6 axes (0 to 5)

# Panels 0 to 4: Individual histograms for 2015–2019
for i, y in enumerate(years):
    ax = axes[i]
    scores = dfs[y]["Score"]
    
    # Plot histogram
    ax.hist(scores, bins=15, color="steelblue", edgecolor="white")
    
    # Add vertical mean and median lines
    mean_val = scores.mean()
    median_val = scores.median()
    ax.axvline(mean_val, color="red", linestyle="--", linewidth=1.5, label=f"mean {mean_val:.2f}")
    ax.axvline(median_val, color="orange", linestyle=":", linewidth=1.5, label=f"median {median_val:.2f}")
    
    # Labels and legend
    ax.set_title(str(y))
    ax.set_xlabel("Happiness Score")
    ax.set_ylabel("Number of countries")
    ax.legend(fontsize=8)

# Panel 5 (Bottom-Right): All years density curve comparison
ax_density = axes[5]
for y in years:
    dfs[y]["Score"].plot(kind="kde", ax=ax_density, label=str(y))

ax_density.set_title("All years (density)")
ax_density.set_xlabel("Happiness Score")
ax_density.set_ylabel("Density")
ax_density.legend(fontsize=9)

# Main overall title and spacing adjustment
fig.suptitle("Task 1 — Distribution of Happiness Score by Year", fontsize=15)
plt.tight_layout()
plt.savefig("plots/task1_score_histograms.png", dpi=150)
plt.close()

print("Combined Task 1 chart saved to 'plots/task1_score_histograms.png'!")