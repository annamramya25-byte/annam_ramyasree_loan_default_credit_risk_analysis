# Loan Default and Credit Risk Analysis

## Project Overview

This project explores loan application and borrower data to identify patterns associated with recorded loan defaults. It uses descriptive analysis and visualizations to summarize repayment outcomes and compare them across borrower and loan characteristics.

The findings describe this dataset only. They are not a validated credit scoring model and should not be used by themselves to approve or reject applicants.

## Project Objectives

- Load and review the loan dataset.
- Clean and validate the data.
- Calculate loan and default metrics.
- Compare default outcomes across loan purpose, employment experience, home ownership, credit score, income, loan amount, and other available fields.
- Present the analysis with Python visualizations and a Power BI dashboard.

## Tools Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Microsoft Power BI Desktop
- Power Query and DAX

## Dataset

The cleaned dataset contains 1,000 records and 17 columns, including:

`Loan_ID`, `Age`, `Annual_Income`, `Employment_Years`, `Loan_Amount`, `Loan_Term_Months`, `Credit_Score`, `Existing_Debt`, `DTI_Ratio`, `Open_Accounts`, `Delinquencies`, `Home_Ownership`, `Loan_Purpose`, `Loan_Grade`, `Interest_Rate`, `Monthly_Payment`, and `Loan_Status`.

The outcome field is `Loan_Status`, with values `Default` and `Paid`.

## Data Cleaning

The Python workflow checks data types, missing values, duplicate records, summary statistics, and possible numerical outliers. It removes duplicate rows, fills missing numerical or categorical values when needed, standardizes loan-status text, and saves a cleaned CSV file.

The supplied cleaned dataset has no missing values and no duplicate rows. Potential outliers are identified for review and are not automatically removed.

## Analysis and Visualizations

The analysis calculates total loans, defaulted loans, paid loans, default rate, and average income, credit score, loan amount, interest rate, and DTI value. It also compares default rates across available categories.

The Python visualization files include:

1. Loan default distribution
2. Loan count by purpose
3. Default rate by purpose
4. Default rate by employment experience
5. Default rate by home ownership
6. Credit score distribution
7. Loan amount distribution
8. Annual income distribution
9. Credit score versus loan amount
10. Income versus loan amount
11. Loan amount by repayment status
12. Credit score by repayment status
13. DTI ratio by repayment status
14. Default rate by income group
15. Correlation heatmap

## Power BI Dashboard

The Power BI report is available as `loan_default_risk_dashboard.pbix`. It presents summary measures and comparisons across available loan and borrower categories. The dataset does not include Region, Gender, Education, or a Previous_Defaults field; those breakdowns cannot be calculated from the supplied columns.

## Key Results

- 1,000 loans are included in the supplied sample.
- 932 loans are labeled `Default` and 68 are labeled `Paid`.
- The observed default rate is 93.20%.
- Average credit score: 685.59.
- Average annual income: 51,733.81 dataset units.
- Average loan amount: 211,514.41 dataset units.
- Vehicle loans have the highest observed default rate by purpose: 95.35% (172 loans).
- Loan Grade F has the highest observed rate among grades: 98.18% (55 loans).

The default share is unusually high. Verify the source data and class balance before drawing operational conclusions. The DTI scale is not documented, so interpret its values only after confirming the units.

## Project Structure

```text
loan_default_credit_risk_analysis/
├── DATASET/
│   └── loan_default_credit_risk_cleaned.csv
├── POWERBI/
│   └── loan_default_risk_dashboard.pbix
├── PYTHON/
│   ├── main.py
│   ├── loan_default_credit_risk_dataset.csv
│   └── visualizations/
│       ├── 01_loan_default_distribution.png
│       ├── 02_loan_count_by_purpose.png
│       └── ...
└── REPORT/
    ├── PROJECT REPORT .PDF3.pdf
    └── BUSINESSINSIGHTS.PDF3.pdf
```

## Run the Python Analysis

1. Install Python 3.
2. Install the required packages:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. Open a terminal in the `PYTHON` folder.
4. Run:

   ```bash
   python main.py
   ```

The script reads `loan_default_credit_risk_dataset.csv`, saves a cleaned CSV, and creates the analysis visualizations.
