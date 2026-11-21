import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Create a folder to save all your generated images cleanly
os.makedirs("plots", exist_ok=True)

years = [2015, 2016, 2017, 2018, 2019]
dfs = {}

# Standardize column names across all 5 files
rename_map = {
    "Country or region": "Country",
    "Happiness Rank": "Rank",
    "Happiness.Rank": "Rank",
    "Overall rank": "Rank",
    "Happiness Score": "Score",
    "Happiness.Score": "Score",
    "Economy (GDP per Capita)": "GDP",
    "Economy..GDP.per.Capita.": "GDP",
    "GDP per capita": "GDP",
    "Family": "Social_Support",
    "Social support": "Social_Support",
    "Health (Life Expectancy)": "Health",
    "Health..Life.Expectancy.": "Health",
    "Healthy life expectancy": "Health",
    "Freedom to make life choices": "Freedom",
    "Trust (Government Corruption)": "Corruption",
    "Trust..Government.Corruption.": "Corruption",
    "Perceptions of corruption": "Corruption"
}

for y in years:
    df = pd.read_csv(f"{y}.csv")
    df = df.rename(columns=rename_map)
    df["Year"] = y
    dfs[y] = df
    print(f"Loaded {y}: {df.shape[0]} countries")