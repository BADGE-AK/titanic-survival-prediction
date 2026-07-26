import requests

from config import API_URL


def predict_passenger(passenger_data: dict):
    """
    Send passenger data to the FastAPI API
    and return the prediction.
    """

    try:

        response = requests.post(
            API_URL,
            json=passenger_data,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:

        return {
            "error": "Could not connect to the FastAPI server."
        }

    except requests.exceptions.Timeout:

        return {
            "error": "The request timed out."
        }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }