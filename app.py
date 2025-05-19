import streamlit as st
import time
from datetime import datetime
from utils.alert_css import ALERT_CSS
from utils.api_client import predict_image, get_alerts

st.set_page_config(page_title="Lumora AI", layout="centered")

st.markdown("<div style='margin-top: 40px'></div>", unsafe_allow_html=True)
st.title("Lumora AI - Crop Disease Detection")

# Sidebar alerts
with st.sidebar:
    st.header("News")

    # CSS for alert styling
    st.markdown(ALERT_CSS, unsafe_allow_html=True)

    # Auto-refresh every 60 seconds
    refresh_interval = 60  # seconds

    if "last_refresh" not in st.session_state:
        st.session_state.last_refresh = datetime.now()

    time_since_refresh = (datetime.now() - st.session_state.last_refresh).total_seconds()

    if time_since_refresh >= refresh_interval:
        st.session_state.last_refresh = datetime.now()
        st.rerun()

    alerts = get_alerts()

    if alerts:
        top_alerts = alerts[:10] 
        for alert in top_alerts:
            st.markdown(
                f'<div class="alert-wrapper"><a href="{alert["link"]}" target="_blank">{alert["title"]}</a></div>',
                unsafe_allow_html=True
            )
    else:
        st.info("No alerts available.")

# Upload and analyze new image
uploaded_file = st.file_uploader("Upload a crop image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze Image"):
        with st.spinner("Sending image..."):
            result = predict_image(uploaded_file, uploaded_file.name, uploaded_file.type)

        if "error" not in result:
            # Simulated typing effect
            def type_writer(label, value, speed=0.02):
                container = st.empty()
                final_text = f"**{label}** {value}"
                output = ""
                plain_text = f"{label} {value}"
                for char in range(len(plain_text)):
                    output = plain_text[:char + 1]
                    container.markdown(f"{output}▌")
                    time.sleep(speed)
                container.markdown(final_text)

            st.markdown("### AI Diagnosis Result")
            type_writer("Disease Detected:", result['disease_name'])
            type_writer("Confidence:", result['confidence'])
            type_writer("Cause:", result['cause'])
            type_writer("Symptoms:", result['symptoms'])
            type_writer("Treatment:", result['treatment'])

            # Added a disclaimer
            st.markdown("""
            <div style="margin-top: 20px; padding: 10px; border-left: 5px solid #FFA500; border-radius: 5px;">
                <strong>Disclaimer:</strong> This is an AI-generated analysis. If symptoms persist or worsen, please consult a qualified agricultural extension officer or plant health expert for further guidance.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(result["error"])
