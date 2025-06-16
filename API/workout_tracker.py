import os
import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 62
HEIGHT_CM = 180
AGE = 20

# os.environ["APP_ID"] = "1d2f22ba"
# os.environ["API_KEY"] = "1cca219ba08c70ebb15e408fe80228e9"

APP_ID = os.environ.get("APP_ID", "does not exist")
API_KEY = os.environ.get("API_KEY", "error")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("sheety_endpoint")

nutritionix_params = {
    "query": input("Tell me which exercise you did? : "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

today = datetime.now()

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=headers)
data = response.json()["exercises"][0]

sheety_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": data["user_input"].title(),
        "duration": data["duration_min"],
        "calories": data["nf_calories"]
    }
}

headers = {
    "Authorization": "Basic c2FsbWFzeWVkMTM2MDpTeWVkYWxpMjAwMCE="
}

response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers)
print(response.text)
