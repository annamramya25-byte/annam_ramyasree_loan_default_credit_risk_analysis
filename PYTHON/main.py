# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv("loan_default_credit_risk_dataset.csv")
print("\n================================================")
print("================================================")

print(df.head())
# ============================================================
# 3. BASIC DATASET INFORMATION
# ============================================================

print("DATASET LOADED SUCCESSFULLY")

# STEP 3: Display the first five records
print("\n================================================")
print("FIRST 5 RECORDS")
print("================================================")
print(df.head())

# STEP 4: Display the last five records
print("\n================================================")
print("LAST 5 RECORDS")
print("================================================")
print(df.tail())

# STEP 5: Check the dataset shape
print("\n================================================")
print("DATASET SHAPE")
print("================================================")

print("Rows and Columns:", df.shape)

# STEP 6: Display all column names
print("\n================================================")
print("COLUMN NAMES")
print("================================================")

print(df.columns)
print("\n================================================")
print("DATA TYPES")
print("================================================")

print(df.dtypes)
print("\n================================================")
print("DATASET INFORMATION")
print("================================================")

df.info()


# ============================================================
# 4. STATISTICAL SUMMARY
# ============================================================

print("\n================================================")
print("STATISTICAL SUMMARY")
print("================================================")

print(df.describe())
print("\n================================================")
print("CATEGORICAL DATA SUMMARY")
print("================================================")

print(df.describe(include="object"))
# STEP 9: Check missing values
print("\n================================================")
print("MISSING VALUES BEFORE CLEANING")
print("================================================")

print(df.isnull().sum())

# ============================================================
# 8. CHECK DUPLICATE RECORDS
# ============================================================

print("\n================================================")
print("DUPLICATE RECORDS")
print("================================================")

print("Duplicate records:", df.duplicated().sum())

# STEP 11: Remove duplicate records
df = df.drop_duplicates().copy()
print("Rows after removing duplicates:", len(df))


# ============================================================
# 5. UNIQUE VALUES
# ============================================================

print("\n================================================")
print("NUMBER OF UNIQUE VALUES")
print("================================================")

for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")

# ============================================================
# 7. HANDLE MISSING VALUES
# ============================================================

print("\n================================================")
print("HANDLING MISSING VALUES")
print("================================================")

# Numeric columns: fill missing values with the median
numeric_columns = df.select_dtypes(include="number").columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Text columns: fill missing values with the most common value
categorical_columns = df.select_dtypes(include="object").columns
for column in categorical_columns:
    if df[column].isnull().any():
        mode_values = df[column].mode()
        if not mode_values.empty:
            df[column] = df[column].fillna(mode_values[0])

print("\nMissing values after filling:")
print(df.isnull().sum())

# STEP 14: Check numerical outliers using the IQR method
print("\n NUMERICAL OUTLIER COUNTS")
for column in numeric_columns:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outlier_count = (
        (df[column] < lower_limit) | (df[column] > upper_limit)
    ).sum()

    print(f"{column}: {outlier_count} possible outliers")

# STEP 15: Verify and save the cleaned dataset
print("\n CLEANED DATASET VERIFICATION")
print("Shape:", df.shape)
print("Remaining missing values:", df.isnull().sum().sum())
print("Remaining duplicate rows:", df.duplicated().sum())

CLEAN_FILE = "loan_default_credit_risk_cleaned.csv"
df.to_csv(CLEAN_FILE, index=False)
print("Cleaned dataset saved to:", CLEAN_FILE)
# ============================================================
# PART 3 — DATA ANALYSIS (STEPS 16–43)
# Run this after loading and cleaning the dataset
# ============================================================

# Make sure the status text is consistent
df["Loan_Status"] = df["Loan_Status"].astype(str).str.strip().str.title()
df["Default_Flag"] = (df["Loan_Status"] == "Default").astype(int)


# STEP 16: Find total customers
print("\n TOTAL CUSTOMERS")
print(df["Loan_ID"].nunique())


# STEP 17: Find total loans
print("\n TOTAL LOANS")
print(len(df))


# STEP 18: Find defaulted loans
print("\n DEFAULTED LOANS")
print(df["Default_Flag"].sum())


# STEP 19: Find non-defaulted loans
print("\n NON-DEFAULTED LOANS")
print((df["Default_Flag"] == 0).sum())


# STEP 20: Calculate overall default rate
print("\n OVERALL DEFAULT RATE")
print(f"{df['Default_Flag'].mean() * 100:.2f}%")


# STEP 21: Calculate average annual income
print("\nAVERAGE ANNUAL INCOME")
print(df["Annual_Income"].mean())


# STEP 22: Calculate average credit score
print("\n AVERAGE CREDIT SCORE")
print(df["Credit_Score"].mean())


# STEP 23: Calculate average loan amount
print("\n AVERAGE LOAN AMOUNT")
print(df["Loan_Amount"].mean())


# STEP 24: Calculate average interest rate
print("\n AVERAGE INTEREST RATE")
print(df["Interest_Rate"].mean())


# STEP 25: Calculate average debt-to-income ratio
print("\n25. AVERAGE DEBT-TO-INCOME RATIO")
print(df["DTI_Ratio"].mean())


# STEP 26: Find number of loans by loan type
# Loan_Purpose is used because the dataset has no Loan_Type column
print("\nLOANS BY LOAN PURPOSE")
print(df["Loan_Purpose"].value_counts())


# STEP 27: Find number of loans by region
print("\n LOANS BY REGION")
if "Region" in df.columns:
    print(df["Region"].value_counts())
else:
    print("Cannot calculate: this dataset has no Region column.")


# STEP 28: Calculate default rate by loan type
# Loan_Purpose is used as the loan-type category
print("\n DEFAULT RATE BY LOAN PURPOSE")
print(
    df.groupby("Loan_Purpose")["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
      .sort_values(ascending=False)
)


# STEP 29: Calculate default rate by employment status
# Employment_Years is grouped as a simple employment-experience proxy
df["Employment_Group"] = pd.cut(
    df["Employment_Years"],
    bins=[-1, 2, 5, 10, float("inf")],
    labels=["0-2 years", "3-5 years", "6-10 years", "10+ years"]
)

print("\n DEFAULT RATE BY EMPLOYMENT EXPERIENCE")
print(
    df.groupby("Employment_Group", observed=False)["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
)


# STEP 30: Calculate default rate by education
print("\n DEFAULT RATE BY EDUCATION")
if "Education" in df.columns:
    print(
        df.groupby("Education")["Default_Flag"]
          .mean()
          .mul(100)
          .round(2)
    )
else:
    print("Cannot calculate: this dataset has no Education column.")


# STEP 31: Calculate default rate by property ownership
print("\n DEFAULT RATE BY HOME OWNERSHIP")
print(
    df.groupby("Home_Ownership")["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
      .sort_values(ascending=False)
)


# STEP 32: Calculate default rate by credit-score group
df["Credit_Score_Group"] = pd.cut(
    df["Credit_Score"],
    bins=[-float("inf"), 579, 669, 739, 799, float("inf")],
    labels=["Poor", "Fair", "Good", "Very Good", "Excellent"]
)

print("\n DEFAULT RATE BY CREDIT-SCORE GROUP")
print(
    df.groupby("Credit_Score_Group", observed=False)["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
)


# STEP 33: Calculate default rate by income group
df["Income_Group"] = pd.qcut(
    df["Annual_Income"],
    q=4,
    labels=["Low", "Lower-Middle", "Upper-Middle", "High"],
    duplicates="drop"
)

print("\nDEFAULT RATE BY INCOME GROUP")
print(
    df.groupby("Income_Group", observed=False)["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
)


# STEP 34: Find customers with below-average credit scores
average_credit_score = df["Credit_Score"].mean()

print("\n CUSTOMERS WITH BELOW-AVERAGE CREDIT SCORES")
print(df[df["Credit_Score"] < average_credit_score][
    ["Loan_ID", "Credit_Score", "Loan_Status"]
].head(20))


# STEP 35: Find customers with above-average loan amounts
average_loan_amount = df["Loan_Amount"].mean()

print("\n CUSTOMERS WITH ABOVE-AVERAGE LOAN AMOUNTS")
print(df[df["Loan_Amount"] > average_loan_amount][
    ["Loan_ID", "Loan_Amount", "Loan_Status"]
].head(20))


# STEP 36: Find customers with high debt-to-income ratios
# Here, DTI above 0.40 is treated as high; adjust if your dataset uses percentages
print("\n LOANS WITH HIGH DTI RATIO (ABOVE 0.40)")
print(df[df["DTI_Ratio"] > 0.40][
    ["Loan_ID", "DTI_Ratio", "Loan_Status"]
].head(20))


# STEP 37: Find top 10 customers based on loan amount
print("\n TOP 10 LOANS BY LOAN AMOUNT")
print(
    df.nlargest(10, "Loan_Amount")[
        ["Loan_ID", "Loan_Amount", "Loan_Status"]
    ]
)


# STEP 38: Find loan purpose with the highest default rate
purpose_default_rate = (
    df.groupby("Loan_Purpose")["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
)

print("\n38. LOAN PURPOSE WITH HIGHEST DEFAULT RATE")
print(purpose_default_rate.idxmax(), "-", purpose_default_rate.max(), "%")


# STEP 39: Find region with highest default rate
print("\n REGION WITH HIGHEST DEFAULT RATE")
if "Region" in df.columns:
    region_default_rate = (
        df.groupby("Region")["Default_Flag"]
          .mean()
          .mul(100)
          .round(2)
    )
    print(region_default_rate.idxmax(), "-", region_default_rate.max(), "%")
else:
    print("Cannot calculate: this dataset has no Region column.")


# STEP 40: Analyze credit score vs default
print("\n AVERAGE CREDIT SCORE BY LOAN STATUS")
print(df.groupby("Loan_Status")["Credit_Score"].mean().round(2))


# STEP 41: Analyze income vs default
print("\n AVERAGE ANNUAL INCOME BY LOAN STATUS")
print(df.groupby("Loan_Status")["Annual_Income"].mean().round(2))


# STEP 42: Analyze loan amount vs default
print("\n AVERAGE LOAN AMOUNT BY LOAN STATUS")
print(df.groupby("Loan_Status")["Loan_Amount"].mean().round(2))


# STEP 43: Check patterns associated with loan default
# Delinquencies is used as a proxy because Previous_Defaults is not available
print("\n DEFAULT PATTERN SUMMARY")

print("\nDefault rate by loan purpose:")
print(
    df.groupby("Loan_Purpose")["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
      .sort_values(ascending=False)
)

print("\nDefault rate by home ownership:")
print(
    df.groupby("Home_Ownership")["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
      .sort_values(ascending=False)
)

print("\nAverage credit score and DTI by loan status:")
print(
    df.groupby("Loan_Status")[["Credit_Score", "DTI_Ratio", "Delinquencies"]]
      .mean()
      .round(2)
)

print("\nPrevious defaults are not available in the dataset.")
print("Delinquencies is shown as a related, but not identical, measure.")
# STEP 43: Identify important patterns associated with loan default

print("\nIMPORTANT PATTERNS ASSOCIATED WITH LOAN DEFAULT")
print("=" * 60)

# 1. Overall default rate
default_rate = (df["Loan_Status"] == "Default").mean() * 100
print(f"Overall default rate: {default_rate:.2f}%")

# 2. Default rate by loan purpose
print("\nDefault rate by loan purpose:")
print(
    df.assign(Default_Flag=(df["Loan_Status"] == "Default").astype(int))
      .groupby("Loan_Purpose")["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
      .sort_values(ascending=False)
)

# 3. Default rate by home ownership
print("\nDefault rate by home ownership:")
print(
    df.assign(Default_Flag=(df["Loan_Status"] == "Default").astype(int))
      .groupby("Home_Ownership")["Default_Flag"]
      .mean()
      .mul(100)
      .round(2)
      .sort_values(ascending=False)
)

# 4. Compare average values for defaulted and paid loans
print("\nAverage values by loan status:")
print(
    df.groupby("Loan_Status")[
        ["Credit_Score", "Annual_Income", "Loan_Amount",
         "DTI_Ratio", "Delinquencies"]
    ]
    .mean()
    .round(2)
)

# 5. Show the strongest correlations with default
df["Default_Flag"] = (df["Loan_Status"] == "Default").astype(int)

numeric_columns = df.select_dtypes(include="number").columns
correlations = (
    df[numeric_columns]
    .corr()["Default_Flag"]
    .drop("Default_Flag")
    .sort_values(key=abs, ascending=False)
)

print("\nNumeric factors most associated with default:")
print(correlations.round(3))
analysis_df = df.groupby("Loan_Status")[["Annual_Income", "Credit_Score", "Loan_Amount"]].mean().round(2)
analysis_df.to_csv("loan_default_credit_risk_analysis.csv")
print("Analysis CSV saved")
# ============================================================
# PART 4 — PYTHON VISUALIZATION
# ============================================================

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Create a folder for the charts
CHART_DIR = Path("visualizations")
CHART_DIR.mkdir(exist_ok=True)

# Make sure loan status is consistent
df["Loan_Status"] = df["Loan_Status"].astype(str).str.strip().str.title()
df["Default_Flag"] = (df["Loan_Status"] == "Default").astype(int)

sns.set_theme(style="whitegrid")


def save_chart(filename):
    """Save the current chart and close it."""
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    print("Saved:", CHART_DIR / filename)


# 1. Loan Default Distribution — Pie Chart
plt.figure(figsize=(6, 6))
df["Loan_Status"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90
)
plt.title("Loan Default Distribution")
plt.ylabel("")
save_chart("01_loan_default_distribution.png")


# 2. Loan Count by Loan Type — Loan_Purpose used as proxy
plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="Loan_Purpose", order=df["Loan_Purpose"].value_counts().index)
plt.title("Loan Count by Loan Purpose")
plt.xlabel("Loan Purpose")
plt.ylabel("Number of Loans")
plt.xticks(rotation=35, ha="right")
save_chart("02_loan_count_by_purpose.png")


# 3. Default Rate by Loan Type — Loan_Purpose used as proxy
purpose_rate = (
    df.groupby("Loan_Purpose")["Default_Flag"].mean().mul(100).sort_values()
)
plt.figure(figsize=(9, 5))
purpose_rate.plot(kind="bar", color="tomato")
plt.title("Default Rate by Loan Purpose")
plt.xlabel("Loan Purpose")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=35, ha="right")
save_chart("03_default_rate_by_purpose.png")


# 4. Default Rate by Employment Status — experience group proxy
df["Employment_Group"] = pd.cut(
    df["Employment_Years"],
    bins=[-1, 2, 5, 10, float("inf")],
    labels=["0–2 years", "3–5 years", "6–10 years", "10+ years"]
)
employment_rate = (
    df.groupby("Employment_Group", observed=False)["Default_Flag"]
      .mean().mul(100)
)
plt.figure(figsize=(8, 5))
employment_rate.plot(kind="bar", color="steelblue")
plt.title("Default Rate by Employment Experience")
plt.xlabel("Employment Experience")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=0)
save_chart("04_default_rate_by_employment_experience.png")


# 5. Default Rate by Education — Home_Ownership used because Education is absent
ownership_rate = (
    df.groupby("Home_Ownership")["Default_Flag"].mean().mul(100).sort_values()
)
plt.figure(figsize=(8, 5))
ownership_rate.plot(kind="bar", color="mediumpurple")
plt.title("Default Rate by Home Ownership")
plt.xlabel("Home Ownership")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=30, ha="right")
save_chart("05_default_rate_by_home_ownership.png")


# 6. Credit Score Distribution — Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Credit_Score", bins=20, kde=True)
plt.title("Credit Score Distribution")
save_chart("06_credit_score_distribution.png")


# 7. Loan Amount Distribution — Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Loan_Amount", bins=20, kde=True)
plt.title("Loan Amount Distribution")
save_chart("07_loan_amount_distribution.png")


# 8. Annual Income Distribution — Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Annual_Income", bins=20, kde=True)
plt.title("Annual Income Distribution")
save_chart("08_annual_income_distribution.png")


# 9. Credit Score vs Loan Amount — Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x="Credit_Score", y="Loan_Amount", hue="Loan_Status"
)
plt.title("Credit Score vs Loan Amount")
save_chart("09_credit_score_vs_loan_amount.png")


# 10. Income vs Loan Amount — Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x="Annual_Income", y="Loan_Amount", hue="Loan_Status"
)
plt.title("Annual Income vs Loan Amount")
save_chart("10_income_vs_loan_amount.png")


# 11. Loan Amount by Default Status — Box Plot
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Loan_Status", y="Loan_Amount")
plt.title("Loan Amount by Loan Status")
save_chart("11_loan_amount_by_status.png")


# 12. Credit Score by Default Status — Box Plot
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Loan_Status", y="Credit_Score")
plt.title("Credit Score by Loan Status")
save_chart("12_credit_score_by_status.png")


# 13. Debt-to-Income Ratio by Default Status — Box Plot
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Loan_Status", y="DTI_Ratio")
plt.title("Debt-to-Income Ratio by Loan Status")
save_chart("13_dti_ratio_by_status.png")


# 14. Default Rate by Income Group — Bar Chart
df["Income_Group"] = pd.qcut(
    df["Annual_Income"],
    q=4,
    labels=["Low", "Lower-Middle", "Upper-Middle", "High"],
    duplicates="drop"
)
income_rate = (
    df.groupby("Income_Group", observed=False)["Default_Flag"].mean().mul(100)
)
plt.figure(figsize=(8, 5))
income_rate.plot(kind="bar", color="darkorange")
plt.title("Default Rate by Income Group")
plt.xlabel("Income Group")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=0)
save_chart("14_default_rate_by_income_group.png")


# 15. Correlation Heatmap
numeric_df = df.select_dtypes(include="number").drop(
    columns=["Default_Flag"], errors="ignore"
)
numeric_df = numeric_df.copy()
numeric_df["Default_Flag"] = df["Default_Flag"]

plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Loan Data Correlation Heatmap")
save_chart("15_correlation_heatmap.png")

print("\nAll visualization charts saved in the visualizations folder.")