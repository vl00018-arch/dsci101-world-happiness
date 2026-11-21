# World Happiness Report Data Analysis (2015–2019)
**Course:** DSCI 101-001 — Introduction to Data Science (West Virginia University)

## Project Overview
This repository contains an exploratory data analysis (EDA) of the World Happiness Report datasets from 2015 to 2019 using Python (`pandas`, `matplotlib`, `seaborn`, and `plotly`) inside the `elation` virtual environment. *(Note: Raw CSV dataset files are excluded per confidentiality guidelines.)*

## Repository Structure
* `data_loader.py` — Loads the 2015–2019 CSV datasets, standardizes column names across years, and maps countries to regions.
* `task1.py` — Histograms and KDE density plots of Happiness Scores by year.
* `task2.py` — 2D scatter plots comparing GDP per Capita and Health (Life Expectancy).
* `task3.py` — 2D scatter plots comparing Freedom and Generosity.
* `task4.py` — 3D scatter plots exploring GDP per Capita, Corruption, and Generosity.
* `task5.py` — Identification of missing/added countries between consecutive years.
* `task6.py` — Pearson, Spearman, and Kendall rank correlation coefficients for selected variable pairs.
* `task7.py` — Correlation ranking identifying the strongest predictors of Happiness Score.
* `task8.py` — Choropleth world map heatmaps of Happiness Scores (2015–2019).
* `task9.py` — Regional happiness rank and score trends across years.
* `plots/` — Generated visualizations and summary CSV tables for Tasks 1–9.

## Key Findings
* **Strongest Predictors (Task 7):** GDP per Capita, Social Support, and Healthy Life Expectancy consistently show the strongest positive correlation with Happiness Score across all five years.
* **Regional Trends (Task 9):** Australia & New Zealand, North America, and Western Europe maintain the highest average happiness rankings from 2015 to 2019, while Sub-Saharan Africa and Southern Asia rank lowest on average.
* **Weak Correlations (Task 6):** Generosity shows very weak correlation with both overall Happiness Score and Freedom across all years.
