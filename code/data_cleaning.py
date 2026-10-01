import pandas as pd
import numpy as np

# Load raw dataset
df = pd.read_csv("data/raw/marketing_campaign_raw.csv", sep=None, engine="python")

# 1. Clean column names
df.columns = (
    df.columns.str.strip()
      .str.lower()
      .str.replace(r"[^a-z0-9]+", "_", regex=True)
      .str.strip("_")
)

# 2. Trim text values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 3. Standardize categorical values
df["education"] = df["education"].replace({"2n Cycle": "2nd Cycle"})
df["marital_status"] = df["marital_status"].replace({
    "Alone": "Single",
    "YOLO": "Single",
    "Absurd": "Unknown"
})

# 4. Handle missing income values with the median
income_median = df["income"].median()
df["income"] = df["income"].fillna(income_median)

# 5. Handle clearly invalid birth years
df.loc[df["year_birth"] < 1940, "year_birth"] = np.nan

# 6. Convert customer date to a consistent datetime format
df["dt_customer"] = pd.to_datetime(
    df["dt_customer"], format="%d-%m-%Y", errors="coerce"
)

# 7. Remove exact duplicate rows
df = df.drop_duplicates()

# 8. Export cleaned dataset
df["dt_customer"] = df["dt_customer"].dt.strftime("%Y-%m-%d")
df.to_csv("data/cleaned/marketing_campaign_cleaned.csv", index=False)

print("Cleaned dataset saved successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Remaining missing values:", int(df.isna().sum().sum()))
print("Duplicate rows:", int(df.duplicated().sum()))
