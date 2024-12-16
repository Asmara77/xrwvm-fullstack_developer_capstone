# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = f"https://n4913819-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai{endpoint}?{params}"


    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")


# def analyze_review_sentiments(text):
def analyze_review_sentiments(text):
    request_url = f"https://sentianalyzer.1pi0wntbws1j.us-south.codeengine.appdomain.cloud/analyze/{text}"

    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

# def post_review(data_dict):
def post_review(data_dict):
    request_url = f"{https://n4913819-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai}/insert_review"

    try:
        response = requests.post(request_url,json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
