import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure output directory exists
os.makedirs("images", exist_ok=True)

years = [2015, 2016, 2017, 2018, 2019]

# Create a 2x3 grid of subplots (5 plots + 1 empty slot)
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

for idx, year in enumerate(years):
    ax = axes[idx]
    df = pd.read_csv(f"{year}.csv")
    df = df.rename(columns={"Freedom to make life choices": "Freedom"})

    # Standardize column names across different years
    if year in [2015, 2016, 2017]:
        country_col = "Country"
    else:  # 2018, 2019
        country_col = "Country or region"

    # Plot Freedom (x-axis) vs. Generosity (y-axis)
    ax.scatter(
        df["Freedom"],
        df["Generosity"],
        alpha=0.7,
        color="#2b7bba",
        edgecolors="white",
        s=50
    )

    # Label top outliers (highest/lowest Freedom and Generosity) to keep plot readable
    outliers = pd.concat([
        df.nlargest(2, "Generosity"),
        df.nlargest(2, "Freedom"),
        df.nsmallest(2, "Freedom")
    ]).drop_duplicates(subset=[country_col])

    for _, row in outliers.iterrows():
        ax.annotate(
            row[country_col],
            (row["Freedom"], row["Generosity"]),
            fontsize=8,
            xytext=(4, 4),
            textcoords="offset points",
            alpha=0.85
        )

    ax.set_title(f"{year}: Freedom vs. Generosity", fontsize=12, fontweight="bold")
    ax.set_xlabel("Freedom")
    ax.set_ylabel("Generosity")
    ax.grid(True, linestyle="--", alpha=0.4)

# Hide the unused 6th subplot (bottom-right)
axes[-1].axis("off")

plt.suptitle(
    "Task 3: Freedom vs. Generosity Across Countries (2015–2019)",
    fontsize=16,
    fontweight="bold",
    y=1.02
)
plt.tight_layout()

# Save the combined figure for your GitHub repo
plt.savefig("images/task3_freedom_vs_generosity_combined.png", dpi=300, bbox_inches="tight")
plt.show()