import streamlit as st
import pandas as pd
import pickle
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "Material_model.pkl"), "rb"))
target_encoder = pickle.load(open(os.path.join(BASE_DIR, "target_encoder.pkl"), "rb"))
le = pickle.load(open(os.path.join(BASE_DIR, "label_encoder.pkl"), "rb"))

st.title("🔧 Engineering Material Selector")
st.write("Enter your requirements and get the best material category!")

max_temp = st.number_input("Maximum Temperature (°C)", min_value=50, max_value=2000, value=300)
tensile_strength = st.number_input("Tensile Strength (MPa)", min_value=10, max_value=2000, value=400)
cost = st.selectbox("Cost", ["Low", "Medium", "High"])
weight = st.selectbox("Weight", ["Light", "Medium", "Heavy"])
corrosion = st.selectbox("Corrosion Resistance", ["Low", "Medium", "High"])

if st.button("🔍 Find Best Material Category"):
    cost_encoded = le.fit_transform([cost])[0]
    weight_encoded = le.fit_transform([weight])[0]
    corrosion_encoded = le.fit_transform([corrosion])[0]
    user_input = pd.DataFrame([[max_temp, tensile_strength, cost_encoded, weight_encoded, corrosion_encoded]],
                               columns=["Max_Temp", "Tensile_Strength", "Cost", "Weight", "Corrosion_Resistance"])
    prediction = model.predict(user_input)
    result = target_encoder.inverse_transform(prediction)[0]
    st.success(f"✅ Recommended Material Category: **{result}**")
    st.balloons()