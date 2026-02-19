import streamlit as st
import requests

# Local API URL for testing — swap to Render URL after deployment
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="ML Deployment Platform", page_icon="🌸")

st.title("🌸 Iris Flower Predictor")
st.markdown("### Powered by FastAPI + Docker + Render")
st.markdown("---")

st.subheader("Enter Flower Measurements:")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.5)

with col2:
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
    petal_width = st.slider("Petal Width (cm)", 0.1, 3.0, 0.2)

st.markdown("---")

if st.button("🔍 Predict", use_container_width=True):
    with st.spinner("Calling ML API..."):
        try:
            response = requests.post(API_URL, json={
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width
            })
            result = response.json()
            st.success(f"🌺 Prediction: **{result['prediction']}**")
            st.info(f"📊 Confidence: **{result['confidence']}%**")
        except Exception as e:
            st.error(f"API Error: {e}")

st.markdown("---")
st.markdown("Built with ❤️ | FastAPI + Docker + Render + Hugging Face")
