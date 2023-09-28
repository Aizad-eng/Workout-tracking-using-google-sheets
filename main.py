import requests
import json
import datetime

NUTRITIONIX_API_KEY = "Nutritionix API KEY"
NUTRITIONIX_APP_ID = "Nutritionix APP ID"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
todays_date = str(datetime.datetime.now().date())
SHEETY_ENDPOINT = "YOUR SHEETY ENDPOINT"

GENDER = #YOUR GENDER
WEIGHT_KG = #YOUR WEIGHT
HEIGHT_CM = #YOUR HEIGHT
AGE = #YOUR AGE

QUERY = input("How many exercises did you do today? ")

body = {
    "query":QUERY,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

headers = {
    "x-app-id":NUTRITIONIX_APP_ID,
    "x-app-key":NUTRITIONIX_API_KEY,
    "Content-Type":"application/json"

}

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=body, headers=headers)
data= nutritionix_response.json()


headers = {'Content-Type': 'application/json'}



for i in range(len(data["exercises"])):
    exercise = data["exercises"][i]["name"]
    duration = data["exercises"][i]["duration_min"]
    calories = data["exercises"][i]["nf_calories"]

    sheet_input = {
    "workout":{
        "date":todays_date,
        "time":"13:00",
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
    }


    sheety_response = requests.post(url= SHEETY_ENDPOINT, json=sheet_input, headers=header)
print(sheety_response.text)
