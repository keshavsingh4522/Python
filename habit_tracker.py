import requests
from datetime import datetime

# User Details

GENDER = "female"
WEIGHT_KG = 60
HEIGHT_CM = 163
AGE = 20

# API keys, tokens

APP_ID = xxx
API_KEY = xx
BEARER_TOKEN = xx

# Endpoints

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/0f259f8056e0368d57410e8f4451e0a2/workoutTracking/workouts"

# Date-Time & Duration Calculations

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Ask user to enter workout details

exercise_details = input("Give me details about your workout: ")

# From Nutritionix

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
 "query": exercise_details,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(
    exercise_endpoint, 
    json=params, 
    headers=headers
)
result = response.json()
print(result)

# From Sheety

bearer_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(sheety_response.text)
