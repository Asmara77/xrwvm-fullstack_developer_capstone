# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('BACKEND_URL', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('SENTIMENT_ANALYZER_URL',
                                   default="http://localhost:5050")


def get_request(endpoint, **kwargs):
    params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = (
        "https://n4913819-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01."
        "proxy.cognitiveclass.ai" + endpoint + "?" + params
    )

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    request_url = (
        "https://sentianalyzer.1pi0wntbws1j.us-south.codeengine."
        "appdomain.cloud/analyze/{text}"
    )

    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def post_review(data_dict):
    request_url = (
        "https://n4913819-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01."
        "proxy.cognitiveclass.ai/insert_review"
    )
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
