# Task 1: Data Cleaning and Preprocessing

## 📌 Internship Task

**Task:** Data Cleaning and Preprocessing  
**Dataset:** Customer Personality Analysis  
**Dataset File:** `marketing_campaign.csv`

---

## 🎯 Objective

The objective of this task is to clean and prepare a raw dataset containing missing values, duplicate records, invalid values, inconsistent categorical values, and date-format issues.

The cleaned dataset is prepared for further data analysis and visualization.

---

## 🛠️ Tools Used

- Python
- Pandas
- NumPy

---

## 📊 Dataset Information

### Before Cleaning

- **Rows:** 2,240
- **Columns:** 29
- **Missing values:** 24
- **Missing `Income` values:** 24
- **Exact duplicate rows:** 0
- **Clearly invalid `Year_Birth` values:** 3

---

## 🧹 Data Cleaning Steps

The following preprocessing steps were performed:

### 1. Standardized Column Names

All column names were converted to lowercase `snake_case` format.

Example:

```text
Year_Birth → year_birth
Marital_Status → marital_status
```

### 2. Removed Unnecessary Whitespace

Leading and trailing whitespace was removed from text/categorical values.

### 3. Standardized Education Values

The inconsistent value:

```text
2n Cycle
```

was standardized to:

```text
2nd Cycle
```

### 4. Standardized Marital Status

Inconsistent categorical values were standardized:

```text
Alone → Single
YOLO → Single
Absurd → Unknown
```

### 5. Handled Missing Income Values

There were **24 missing values** in the `Income` column.

The missing values were filled using the **median income**:

```text
Median Income = 51,381.5
```

### 6. Handled Invalid Birth Years

Three clearly invalid `Year_Birth` values were identified:

```text
1893
1899
1900
```

These values were replaced with missing values rather than inventing replacement birth years.

### 7. Standardized Date Format

The `Dt_Customer` column was converted from the original:

```text
dd-mm-yyyy
```

format into a consistent date representation and exported as:

```text
yyyy-mm-dd
```

### 8. Checked and Removed Duplicate Records

Duplicate records were checked using Pandas.

No exact duplicate rows were found in the original dataset.

---

## 🔍 Data Quality Checks

The dataset was checked for:

- Missing values
- Duplicate records
- Invalid birth-year values
- Inconsistent categorical values
- Date-format consistency
- Column-name consistency
- Data types

---

## 📈 Results After Cleaning

- **Rows:** 2,240
- **Columns:** 29
- **Remaining missing values:** 3
- **Remaining duplicate rows:** 0

The remaining 3 missing values correspond to the three invalid birth-year values that were intentionally converted to missing values.

---

## 📁 Project Structure

```text
Task-01-Data-Cleaning/
│
├── data/
│   ├── raw/
│   │   └── marketing_campaign_raw.csv
│   │
│   └── cleaned/
│       └── marketing_campaign_cleaned.csv
│
├── code/
│   └── data_cleaning.py
│
├── screenshots/
│   ├── 01_before_cleaning.png
│   ├── 02_cleaning_steps.png
│   └── 03_after_cleaning.png
│
└── README.md
```

---

## 📂 Output

The cleaned dataset is available at:

```text
data/cleaned/marketing_campaign_cleaned.csv
```

---

## 📝 Summary

The raw Customer Personality Analysis dataset was cleaned and preprocessed using Python, Pandas, and NumPy.

Missing values, duplicate records, invalid birth-year values, inconsistent categorical values, column names, and date formats were checked and handled appropriately.

The resulting dataset is cleaner, more consistent, and ready for further data analysis or visualization.

---

## 🎓 Learning Outcome

Through this task, I gained practical experience in:

- Identifying missing values
- Handling missing data
- Detecting duplicate records
- Standardizing categorical data
- Cleaning column names
- Handling invalid values
- Converting date formats
- Performing basic data-quality checks
- Preparing a dataset for further analysis
