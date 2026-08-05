import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------------
# Load Dataset
# ------------------------------------

df = pd.read_csv("cleaned_train.csv")

# Remove Loan_ID
df.drop("Loan_ID", axis=1, inplace=True)

# ------------------------------------
# Encode Categorical Columns
# ------------------------------------

label_encoders = {}

categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

for col in categorical_columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le

# ------------------------------------
# Features and Target
# ------------------------------------

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]

# ------------------------------------
# Split Dataset
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ------------------------------------
# Scale Data
# ------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# ------------------------------------
# Train Random Forest
# ------------------------------------

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

model.fit(X_train, y_train)

# ------------------------------------
# Prediction
# ------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", round(accuracy * 100,2),"%")

print("\nConfusion Matrix")

print(confusion_matrix(y_test,y_pred))

print("\nClassification Report")

print(classification_report(y_test,y_pred))

# ------------------------------------
# Feature Importance
# ------------------------------------

importance = pd.DataFrame({

    "Feature":X.columns,

    "Importance":model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance\n")

print(importance)

# ------------------------------------
# Save Files
# ------------------------------------

joblib.dump(model,"credit_model.pkl")

joblib.dump(label_encoders,"label_encoders.pkl")

joblib.dump(scaler,"scaler.pkl")

print("\nModel Saved Successfully.")