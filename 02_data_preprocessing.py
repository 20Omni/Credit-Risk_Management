import pandas as pd

# Load dataset
df = pd.read_csv("train.csv")

# -----------------------------
# Display Missing Values Before Preprocessing
# -----------------------------
print("Missing Values Before Preprocessing:")
print(df.isnull().sum())

# -----------------------------
# Handle Missing Values
# -----------------------------

# Fill categorical values with mode
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

# Fill numerical values
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

# -----------------------------
# Feature Engineering
# -----------------------------

# Total income of applicant
df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]

# Loan to Income Ratio
df["LoanIncomeRatio"] = df["LoanAmount"] / (df["TotalIncome"] + 1)

# Estimated EMI
df["EstimatedEMI"] = df["LoanAmount"] / df["Loan_Amount_Term"]

# -----------------------------
# Display Missing Values After Preprocessing
# -----------------------------
print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())

# -----------------------------
# Preview New Features
# -----------------------------
print("\nNew Features Added:")
print(df[["TotalIncome", "LoanIncomeRatio", "EstimatedEMI"]].head())

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("cleaned_train.csv", index=False)

print("\n✅ Data preprocessing completed successfully.")
print("✅ Cleaned dataset saved as 'cleaned_train.csv'")