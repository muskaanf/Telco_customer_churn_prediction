import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

st.title('Customer Churn Prediction')

try:
    total_charges = float(st.text_input('Total Charges:', '0'))
    monthly_charges = float(st.text_input('Monthly Charges:', '0'))
    tenure = float(st.text_input('Tenure:', '0'))
except ValueError as e:
    st.error("Please enter valid numbers for Monthly Charges, Tenure, and Total Charges.")
    st.stop()

contract = st.selectbox('Select Contract Type', ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox('Select Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'])
online_security = st.radio('Do you have Online Security?', ['Yes', 'No'])
tech_support = st.radio('Do you have Tech Support?', ['Yes', 'No'])
gender = st.radio('Gender:', ['Female', 'Male'])
online_backup = st.radio('Do you have Online Backup?', ['Yes', 'No'])
internet_service= st.selectbox('Internet Service Type', ['DSL', 'Fiber Optic', 'No'])
paperless_billing = st.radio('Paperless Billing:', ['Yes', 'No'])


contract_dict = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
contract = contract_dict[contract]
payment_method_dict = {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}
payment_method = payment_method_dict[payment_method]
online_security = 1 if online_security == 'Yes' else 0
tech_support = 1 if tech_support == 'Yes' else 0
gender = 1 if gender == 'Male' else 0
online_backup = 1 if online_backup == 'Yes' else 0
internet_service_dict = {'DSL': 0, 'Fiber Optic': 1, 'No': 2}
internet_service = internet_service_dict[internet_service]
paperless_billing = 1 if paperless_billing == 'Yes' else 0

numerical_features = np.array([[monthly_charges, tenure, total_charges]])
categorical_features = np.array([
    contract, payment_method, online_security, tech_support, gender, online_backup, internet_service, paperless_billing
])

input_data = np.concatenate((numerical_features, categorical_features.reshape(1, -1)), axis=1)

if input_data.shape[1] != model.n_features_in_:
    st.error(f"Expected {model.n_features_in_} features, but got {input_data.shape[1]}.")
else:
    
    input_data_scaled = scaler.transform(input_data)
    
    prediction = model.predict(input_data_scaled)
    # st.write(f'Prediction: {prediction[0]}')

    if st.button('Predict'):
        st.write(f'Prediction: {prediction[0]}')
