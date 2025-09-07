import streamlit as st
import requests
import time 

API_URL = "https://crop-recommendation-system-16.onrender.com/predict" 

st.set_page_config(page_title="🌱 Crop Recommendation System", layout="centered")

st.title("🌱 Crop Recommendation System")
st.markdown("Enter your soil and weather details below:")



Nitrogen=st.number_input("Nitrogen(N)")
Phosphorus=st.number_input("Phosphorus(P)")
Potassium=st.number_input("Potassium(K)")
Temperature=st.number_input("Temperature")
Humidity=st.number_input("Humidity %")
pH_value=st.number_input("pH value ")
Rainfall=st.number_input("Rainfall (mm) ")

if st.button("Reccommend Crop"):
    input_data = {
        "N": Nitrogen,
        "P": Phosphorus,
        "K": Potassium,
        "temperature": Temperature,
        "humidity": Humidity,
        "ph": pH_value,
        "rainfall": Rainfall
    }

    with st.spinner("Analyzing your soil and weather conditions..."):
        time.sleep(1)
        try:
            response=requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                result=response.json()
                st.success(f"Recommended Crop : **{result['predicted crop']}**")
            else:
                st.error(f"API Error: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")

