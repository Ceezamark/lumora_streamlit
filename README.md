# Lumora Streamlit Frontend

This project is a Streamlit-based frontend for the Lumora AI Crop Disease API, which is built with Django. The frontend provides an easy-to-use interface for users to interact with the API and receive crop disease predictions and related information.

## Features
- User-friendly web interface built with Streamlit
- Connects to the Lumora AI Crop Disease API (Django backend)
- Allows users to submit crop images and receive disease predictions
- Displays results and recommendations in real-time

## Getting Started

### Prerequisites
- Python 3.x
- pip


### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Ceezamark/lumora_streamlit.git
   cd lumora_streamlit
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Make sure the Lumora AI Crop Disease API (Django backend) is running and accessible.
2. Start the Streamlit frontend:
   ```bash
   streamlit run app.py
   ```
3. Open the provided local URL in your browser to use the app.

## Project Structure
- `app.py`: Main Streamlit application file
- `utils/`: Utility modules for API connection and UI enhancements
  - `api_client.py`: Handles communication with the Django API
  - `alert_css.py`: Custom CSS for alerts and UI styling
- `requirements.txt`: Python dependencies

## About
This frontend was built to make the Lumora AI Crop Disease API accessible to users via a simple web interface. Users can upload crop images, get instant disease predictions, and receive actionable recommendations to manage crop health.

## License
This project is for demonstration purposes only. It is not licensed for commercial or production use.
