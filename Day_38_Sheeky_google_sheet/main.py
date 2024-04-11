import requests
from datetime import datetime as dt
import json
import os 


app_id = os.environ.get("NE_APP_ID")
app_key = os.environ.get("NE_APP_KEY")


end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id" : app_id,
    "x-app-key" : app_key
}

exercise = input("What did you exercise : ")

body = {
    "query" : exercise,
    "gender" : "male",
    "weight_kg" : 74,
    "height_cm" : 169,
    "age" : 21
}

response = requests.post(url=end_point,json=body,headers=header)

result = response.json()

today = dt.now()
format_td = today.strftime("%x")
time = today.strftime("%X")

print(format_td)
print(time)

end_point_sheety = "https://api.sheety.co/7b531558897c8ea66ebda08cb5bcf809/myworkouts/workouts"

for exercise in result["exercises"]:
    body_sheety = {
        "workout":{
            "date" : format_td,
            "time" : time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    auth_token = os.environ.get("work_out_sheety")
    header = {
    "Authorization": f"Basic {auth_token}"
    }
    response = requests.post(url=end_point_sheety,json=body_sheety,headers=header)
    print(response.text)