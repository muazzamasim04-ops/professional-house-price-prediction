import streamlit as st
import joblib
import numpy as np

# Page Configuration (Professional Wide Layout)
st.set_page_config(page_title="Real Estate Valuation System", page_icon="🏡", layout="wide")

# Load Trained Model
@st.cache_resource
def load_model():
    return joblib.load('house_model.joblib')

model = load_model()

# Custom Professional UI Styling
st.markdown("""
    <style>
    .main-header { font-size: 30px; font-weight: bold; color: #1f77b4; }
    .sub-text { font-size: 15px; color: #666; }
    .stButton>button { width: 100%; background-color: #2b5797; color: white; font-weight: bold; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="main-header">🏡 Professional Real Estate Valuation System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Evolvix AI/ML Capstone Project | Intelligent Property Pricing & Market Insights Dashboard</p>', unsafe_allow_html=True)
st.write("---")

# Layout Columns for Professional Dashboard
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("📍 Property Parameters")
    st.write("Enter the exact property details for precise market valuation:")
    
    # Professional Input Controls
    med_inc = st.slider('Median Area Income (in $10k)', min_value=0.5, max_value=15.0, value=4.5, step=0.1)
    house_age = st.slider('Property Age (Years)', min_value=1.0, max_value=52.0, value=10.0, step=1.0)
    ave_rooms = st.slider('Average Rooms per House', min_value=1.0, max_value=10.0, value=5.5, step=0.1)
    ave_bedrms = st.slider('Average Bedrooms', min_value=0.5, max_value=5.0, value=1.2, step=0.1)
    population = st.number_input('Local Area Population', min_value=10, max_value=40000, value=650)
    households = st.number_input('Total Households in Area', min_value=1, max_value=10000, value=220)
    latitude = st.number_input('Location Latitude', value=34.05)
    longitude = st.number_input('Location Longitude', value=-118.24)

with col2:
    st.subheader("📊 Valuation & Market Analysis")
    st.info("This AI dashboard uses advanced **Random Forest Regression** algorithms to estimate real estate market prices dynamically based on location and structural parameters.")
    
    st.write("###")
    
    # Prediction Action
    if st.button('🚀 Calculate Estimated Market Price'):
        # Input Array mapping exactly to training features
        input_data = np.array([[longitude, latitude, house_age, ave_rooms, ave_bedrms, population, households, med_inc]])
        
        # Prediction
        prediction = model.predict(input_data)
        final_price = prediction[0]
        
        # Professional Success Display
        st.success("✅ Property Valuation Completed Successfully!")
        st.metric(label="🏷️ Estimated Property Value", value=f"${final_price:,.2f}")
        
        st.balloons()
