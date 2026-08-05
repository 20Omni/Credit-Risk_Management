# 💳 AI-Based Credit Risk Assessment System

## 📌 Project Overview

The AI-Based Credit Risk Assessment System is a Machine Learning application developed to estimate the credit risk of loan applicants. The system analyzes applicant information such as income, loan amount, employment status, education, credit history, and property area to classify applicants as **Low Credit Risk** or **High Credit Risk**.

The project uses the **Random Forest Classifier** for prediction and provides an interactive web interface built with **Streamlit**.

---

## 🚀 Live Deployment

🌐 **Live Application:** https://credit-risk-management-2pbn.onrender.com/

🔗 **GitHub Repository:** https://github.com/20Omni/Credit-Risk_Management

---

## 🎯 Objectives

- Predict the credit risk of loan applicants.
- Assist financial institutions in preliminary loan assessment.
- Reduce manual evaluation time.
- Demonstrate the application of Machine Learning in banking.

---

## 🛠️ Technologies Used

- Python 3.10
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Dataset

**Dataset Name:** Loan Prediction Dataset

The dataset contains information about loan applicants, including:

- Gender
- Marital Status
- Dependents
- Education
- Self Employment
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area
- Loan Status (Target)

---

## ⚙️ Project Workflow

1. Data Exploration
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Credit Risk Prediction
7. Streamlit Web Application

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Missing value handling
- Categorical data encoding
- Feature scaling
- Dataset cleaning

---

## 📊 Feature Engineering

Additional features created:

- Total Income
- Loan Income Ratio
- Estimated EMI

These features improve the prediction capability of the model.

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

### Model Evaluation

- Accuracy: **78.86%**

The trained model is saved using Joblib for deployment.

---

## 💻 Application Features

- User-friendly Streamlit interface
- Real-time credit risk prediction
- Confidence score display
- Customer information summary
- Fast prediction using a trained Machine Learning model

---

## 📁 Project Structure

```
Credit-Risk-Assessmen/
│
├── train.csv
├── cleaned_train.csv
│
├── 01_data_exploration.py
├── 02_data_preprocessing.py
├── 03_model_training.py
├── 04_app.py
│
├── credit_model.pkl
├── label_encoders.pkl
├── scaler.pkl
│
├── requirements.txt
├── README.md
├── Project_Report.pdf
└── Project_Presentation.pptx
```

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd Credit-Risk-Assessmen
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1

Run preprocessing

```bash
python 02_data_preprocessing.py
```

### Step 2

Train the model

```bash
python 03_model_training.py
```

### Step 3

Launch the Streamlit application

```bash
streamlit run 04_app.py
```

---

## 📷 Screenshots

Add screenshots here after running the application.

- Home Page
- Low Credit Risk Prediction
- High Credit Risk Prediction

---

## 🔮 Future Scope

- Integration with banking databases
- Support for multiple Machine Learning algorithms
- Explainable AI (XAI) using SHAP
- Cloud deployment
- Loan recommendation system

---

## 👨‍💻 Developer

**Omni Sharma**

B.Tech Artificial Intelligence & Machine Learning

VIT Bhopal University

---

## 📄 License

This project is developed for educational purposes.
