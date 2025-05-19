import requests

BASE_URL = "http://127.0.0.1:8000/api"

def predict_image(file, filename, filetype="image/jpeg"):
    """Sends image file to the prediction API and returns parsed JSON response."""
    files = {
        'image': (filename, file, filetype)
    }

    try:
        response = requests.post(f"{BASE_URL}/predict/", files=files)
        response.raise_for_status()  # raises HTTPError if not 2xx

        # Safely parse JSON
        return response.json().get("data", {})
    
    except requests.exceptions.HTTPError:
        try:
            return {"error": response.json().get("error", "Server returned an error.")}
        except Exception:
            return {"error": "Server returned an error (non-JSON response)."}

    except Exception as e:
        return {"error": str(e)}

def get_alerts():
    try:
        res = requests.get(f"{BASE_URL}/alerts/")
        return res.json() if res.status_code == 200 else []
    except Exception:
        return []
