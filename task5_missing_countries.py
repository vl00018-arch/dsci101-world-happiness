import pandas as pd

years = [2015, 2016, 2017, 2018, 2019]
country_sets = {}

# Load the set of countries for each year
for year in years:
    df = pd.read_csv(f"{year}.csv")
    
    # Standardize the country column name
    country_col = "Country" if year in [2015, 2016, 2017] else "Country or region"
    
    # Strip any accidental whitespace and store as a set
    country_sets[year] = set(df[country_col].str.strip())

# Compare consecutive years
results = []
for i in range(len(years) - 1):
    y1 = years[i]
    y2 = years[i + 1]
    
    missing_in_y2 = sorted(country_sets[y1] - country_sets[y2])
    added_in_y2 = sorted(country_sets[y2] - country_sets[y1])
    results.extend(
        {"Comparison": f"{y1} vs {y2}", "Country": country, "Status": f"missing in {y2}"}
        for country in missing_in_y2
    )
    results.extend(
        {"Comparison": f"{y1} vs {y2}", "Country": country, "Status": f"new in {y2}"}
        for country in added_in_y2
    )
    
    print("=" * 60)
    print(f"Comparison: {y1} ({len(country_sets[y1])} countries) vs. {y2} ({len(country_sets[y2])} countries)")
    print("-" * 60)
    print(f"In {y1} but MISSING in {y2} ({len(missing_in_y2)}):")
    print(missing_in_y2 if missing_in_y2 else "None")
    
    print(f"\nIn {y2} but MISSING in {y1} ({len(added_in_y2)}):")
    print(added_in_y2 if added_in_y2 else "None")
    print("=" * 60 + "\n")

pd.DataFrame(results).to_csv("task5_missing_countries.csv", index=False)
print("Saved results to task5_missing_countries.csv")