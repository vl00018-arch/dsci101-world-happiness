import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure output directory exists
os.makedirs("images", exist_ok=True)

years = [2015, 2016, 2017, 2018, 2019]

# Create a 2x3 grid of 3D subplots
fig = plt.figure(figsize=(20, 12))

for idx, year in enumerate(years):
    ax = fig.add_subplot(2, 3, idx + 1, projection="3d")
    df = pd.read_csv(f"{year}.csv")

    df = df.rename(columns={
        "Country or region": "Country",
        "Economy (GDP per Capita)": "GDP",
        "Economy..GDP.per.Capita.": "GDP",
        "GDP per capita": "GDP",
        "Trust (Government Corruption)": "Corruption",
        "Trust..Government.Corruption.": "Corruption",
        "Perceptions of corruption": "Corruption",
    })

    gen_col = "Generosity"
    country_col = "Country"
    gdp_col = "GDP"
    corr_col = "Corruption"

    # Drop rows with missing values (e.g., 2018 has a NaN in Corruption)
    df_clean = df[[country_col, gdp_col, corr_col, gen_col]].dropna()

    # Create 3D scatter plot
    ax.scatter(
        df_clean[gdp_col],
        df_clean[corr_col],
        df_clean[gen_col],
        c=df_clean[gdp_col],
        cmap="viridis",
        s=45,
        alpha=0.8,
        edgecolors="white"
    )

    # Label notable outliers in 3D space (top extremes for each axis)
    outliers = pd.concat([
        df_clean.nlargest(2, gdp_col),
        df_clean.nlargest(2, corr_col),
        df_clean.nlargest(2, gen_col),
        df_clean.nsmallest(1, gdp_col)
    ]).drop_duplicates(subset=[country_col])

    for _, row in outliers.iterrows():
        ax.text(
            row[gdp_col],
            row[corr_col],
            row[gen_col],
            row[country_col],
            fontsize=8,
            color="black"
        )

    ax.set_title(f"{year}: GDP, Corruption & Generosity", fontsize=12, fontweight="bold")
    ax.set_xlabel("GDP per Capita", fontsize=9)
    ax.set_ylabel("Corruption", fontsize=9)
    ax.set_zlabel("Generosity", fontsize=9)

plt.suptitle(
    "Task 4: 3D Relationship Among GDP per Capita, Corruption, and Generosity (2015–2019)",
    fontsize=16,
    fontweight="bold",
    y=0.98
)
plt.tight_layout()

# Save the combined 3D figure for your GitHub repo
plt.savefig("images/task4_3d_gdp_corruption_generosity.png", dpi=300, bbox_inches="tight")
plt.show()