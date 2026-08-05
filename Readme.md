# 💳 AI-Based Credit Risk Assessment System

## 📌 Project Overview

The **AI-Based Credit Risk Assessment System** is a Machine Learning application designed to predict the credit risk of loan applicants. The system analyzes applicant information such as income, loan amount, employment status, education, credit history, and property area to classify applicants as **Low Credit Risk** or **High Credit Risk**.

The application is powered by a **Random Forest Classifier** and provides an interactive web interface built using **Streamlit** for real-time predictions.

---

## 🚀 Live Deployment

🌐 **Live Application:** https://credit-risk-management-2pbn.onrender.com/

💻 **GitHub Repository:** https://github.com/20Omni/Credit-Risk_Management

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

The dataset contains the following applicant information:

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

The following preprocessing techniques were applied:

- Missing value handling
- Categorical variable encoding
- Feature scaling
- Dataset cleaning

---

## 📊 Feature Engineering

Additional features created:

- Total Income
- Loan Income Ratio
- Estimated EMI

These engineered features improve the prediction performance of the machine learning model.

---

## 🤖 Machine Learning Model

### Algorithm Used

- Random Forest Classifier

### Model Performance

- **Accuracy:** **78.86%**

The trained model is serialized using **Joblib** and integrated into the Streamlit application for real-time prediction.

---

## 💻 Application Features

- AI-powered credit risk prediction
- Interactive Streamlit dashboard
- Real-time prediction
- Confidence score display
- Customer information summary
- Fast and accurate loan assessment
- User-friendly interface

---

## 📁 Project Structure

```text
Credit-Risk_Management/
│
├── train.csv
├── cleaned_train.csv
├── 01_data_exploration.py
├── 02_data_preprocessing.py
├── 03_model_training.py
├── 04_app.py
├── credit_model.pkl
├── label_encoders.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── Credit Risk Management PPT.pdf
└── Report Risk Management.docx
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/20Omni/Credit-Risk_Management.git
```

Navigate to the project directory:

```bash
cd Credit-Risk_Management
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1 – Data Preprocessing

```bash
python 02_data_preprocessing.py
```

### Step 2 – Train the Model

```bash
python 03_model_training.py
```

### Step 3 – Launch the Streamlit Application

```bash
streamlit run 04_app.py
```

---

## ☁️ Deployment

The application has been successfully deployed using **Render**.

### Deployment Platform

- Render

### Live Demo

🌐 https://credit-risk-management-2pbn.onrender.com/

---

## 🔮 Future Scope

- Integration with banking databases
- Support for additional Machine Learning algorithms
- Explainable AI (XAI) using SHAP
- Cloud database integration
- Loan recommendation system
- Mobile application support

---

## 👨‍💻 Developer

**Omni Sharma**

B.Tech – Artificial Intelligence & Machine Learning

VIT Bhopal University

---

## 📄 License

This project is developed for educational and learning purposes only.
