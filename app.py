import streamlit as st
import pandas as pd
import joblib


# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
)

# ==========================================
# Load Model
# ==========================================
model = joblib.load("models/customer_churn_pipeline.pkl")

# ==========================================
# Title
# ==========================================
st.title("📊 Customer Churn Prediction")

st.markdown("""
Predict whether a customer is likely to churn based on demographic,
service, and account information.
""")

# ==========================================
# Sidebar
# ==========================================
with st.sidebar:

    st.header("📌 Project Summary")

    st.success("End-to-End Data Science & Machine Learning Project")

    st.markdown("""
### Workflow

- 🧹 Data Cleaning
- 📊 Exploratory Data Analysis
- ⚙️ Data Preprocessing
- 🤖  Model Training
- ⚖️ Threshold Optimization (0.40)
- 🚀 Streamlit Deployment
""")

    st.divider()

    st.subheader("📈 Final Model")

    st.write("**Balanced Logistic Regression**")

    st.write("Decision Threshold: **0.40**")

    st.divider()

    st.subheader("🛠 Technologies")

    st.markdown("""
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
""")

st.divider()

# ==========================================
# Layout
# ==========================================
col1, col2 = st.columns(2)

# ==========================================
# Left Column
# ==========================================
with col1:

    st.subheader("👤 Personal Information")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"],
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"],
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"],
    )

    st.divider()

    st.subheader("📡 Services")

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"],
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No phone service", "No", "Yes"],
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"],
    )

    online_security = st.selectbox(
        "Online Security",
        ["No internet service", "No", "Yes"],
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No internet service", "No", "Yes"],
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No internet service", "No", "Yes"],
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No internet service", "No", "Yes"],
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No internet service", "No", "Yes"],
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No internet service", "No", "Yes"],
    )

# ==========================================
# Right Column
# ==========================================
with col2:

    st.subheader("💳 Account Information")

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12,
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0,
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=800.0,
    )

    st.divider()

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"],
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"],
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)",
        ],
    )

# ==========================================
# Prediction
# ==========================================
st.divider()

if st.button("🔮 Predict Churn", use_container_width=True):

    customer_data = pd.DataFrame(
        {
            "gender": [gender],
            "SeniorCitizen": [1 if senior_citizen == "Yes" else 0],
            "Partner": [partner],
            "Dependents": [dependents],
            "tenure": [tenure],
            "PhoneService": [phone_service],
            "MultipleLines": [multiple_lines],
            "InternetService": [internet_service],
            "OnlineSecurity": [online_security],
            "OnlineBackup": [online_backup],
            "DeviceProtection": [device_protection],
            "TechSupport": [tech_support],
            "StreamingTV": [streaming_tv],
            "StreamingMovies": [streaming_movies],
            "Contract": [contract],
            "PaperlessBilling": [paperless_billing],
            "PaymentMethod": [payment_method],
            "MonthlyCharges": [monthly_charges],
            "TotalCharges": [total_charges],
        }
    )

    probability = model.predict_proba(customer_data)[0][1]

    threshold = 0.40

    prediction = probability >= threshold

    st.divider()

    st.subheader("📈 Prediction Result")

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}",
        delta=f"{probability - threshold:+.2%} vs Threshold"
    )

    st.progress(float(probability))

    st.write(f"**Decision Threshold:** {threshold:.0%}")

    st.divider()

    if prediction:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is not likely to churn.")

    if probability < 0.30:
        st.success("🟢 Risk Level: Low")
    elif probability < 0.60:
        st.warning("🟡 Risk Level: Medium")
    else:
        st.error("🔴 Risk Level: High")

    st.divider()

    st.subheader("💡 Recommendation")

    if prediction:
        st.info(
            """
This customer has a high probability of churning.

Recommended actions:

- Offer a promotional discount.
- Encourage switching to a long-term contract.
- Contact the customer proactively.
- Provide loyalty rewards.
"""
        )
    else:
        st.success(
            """
This customer appears to be loyal.

Recommended actions:

- Continue providing quality service.
- Maintain customer satisfaction.
- Consider loyalty programs for long-term retention.
"""
        )

        