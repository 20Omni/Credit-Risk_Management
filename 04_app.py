
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("credit_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Smart Loan Risk Dashboard", page_icon="💳", layout="wide")

st.markdown("""
<style>
.main {background:#f8fafc;}
.block-container {padding-top:1.5rem;}
.card{
background:white;
padding:18px;
border-radius:12px;
border:1px solid #dbe4f0;
box-shadow:0 2px 8px rgba(0,0,0,.08);
}
.bigtitle{
text-align:center;
font-size:38px;
font-weight:bold;
color:#0d6efd;
}
.subtitle{
text-align:center;
color:#666;
margin-bottom:20px;
}
</style>
""",unsafe_allow_html=True)

st.sidebar.title("🏦 Loan Risk Dashboard")
st.sidebar.success("Model : Random Forest")
st.sidebar.info("Enter applicant information and generate a credit risk assessment.")

st.markdown('<div class="bigtitle">💳 Smart Loan Risk Dashboard</div>',unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered assessment using a trained Random Forest model</div>',unsafe_allow_html=True)

left,right=st.columns(2)

with left:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.subheader("👤 Applicant Information")
    gender=st.selectbox("Gender",["Male","Female"])
    married=st.selectbox("Marital Status",["Yes","No"])
    dependents=st.selectbox("Dependents",["0","1","2","3+"])
    education=st.selectbox("Education",["Graduate","Not Graduate"])
    self_employed=st.selectbox("Self Employed",["Yes","No"])
    property_area=st.selectbox("Property Area",["Urban","Semiurban","Rural"])
    st.markdown("</div>",unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.subheader("💰 Financial Information")
    applicant_income=st.number_input("Applicant Income",min_value=0,value=5000)
    coapplicant_income=st.number_input("Co-applicant Income",min_value=0.0,value=0.0)
    loan_amount=st.number_input("Loan Amount",min_value=0.0,value=150.0)
    loan_term=st.number_input("Loan Term (Months)",min_value=1.0,value=360.0)
    credit_history=st.selectbox("Credit History",[1.0,0.0],format_func=lambda x:"Good" if x==1 else "Poor")
    st.markdown("</div>",unsafe_allow_html=True)

st.markdown("")

if st.button("🚀 Generate Assessment",use_container_width=True):
    df=pd.DataFrame({
        "Gender":[gender],
        "Married":[married],
        "Dependents":[dependents],
        "Education":[education],
        "Self_Employed":[self_employed],
        "ApplicantIncome":[applicant_income],
        "CoapplicantIncome":[coapplicant_income],
        "LoanAmount":[loan_amount],
        "Loan_Amount_Term":[loan_term],
        "Credit_History":[credit_history],
        "Property_Area":[property_area]
    })

    for c in ["Gender","Married","Dependents","Education","Self_Employed","Property_Area"]:
        df[c]=label_encoders[c].transform(df[c])

    df["TotalIncome"]=df["ApplicantIncome"]+df["CoapplicantIncome"]
    df["LoanIncomeRatio"]=df["LoanAmount"]/(df["TotalIncome"]+1)
    df["EstimatedEMI"]=df["LoanAmount"]/df["Loan_Amount_Term"]

    X=scaler.transform(df)
    pred=model.predict(X)[0]
    prob=model.predict_proba(X)[0]
    conf=max(prob)*100

    st.markdown("---")
    st.subheader("📊 Assessment Result")

    a,b=st.columns([2,1])

    with a:
        if pred==1:
            st.success("🟢 LOW CREDIT RISK")
            st.info("Recommendation: Loan can be approved.")
        else:
            st.error("🔴 HIGH CREDIT RISK")
            st.warning("Recommendation: Loan approval is risky.")

    with b:
        st.metric("Confidence",f"{conf:.2f}%")

    st.subheader("📋 Customer Summary")
    summary=pd.DataFrame({
        "Field":["Gender","Marital Status","Education","Dependents","Self Employed","Applicant Income","Co-applicant Income","Loan Amount","Loan Term","Credit History","Property Area"],
        "Value":[gender,married,education,dependents,self_employed,f"₹ {applicant_income}",f"₹ {coapplicant_income}",loan_amount,f"{loan_term} Months","Good" if credit_history==1 else "Poor",property_area]
    })
    st.dataframe(summary,use_container_width=True,hide_index=True)

st.markdown("---")
st.markdown("<center><b>Smart Loan Risk Dashboard</b><br>Python • Streamlit • Scikit-learn • Random Forest</center>",unsafe_allow_html=True)