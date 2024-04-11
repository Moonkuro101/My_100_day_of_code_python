import requests
import time
import smtplib
from datetime import datetime
latitude = 13.905047
longitude = 100.387568
def Iss_location():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    latitude_iss = float(data_iss["iss_position"]["latitude"])
    longitude_iss = float(data_iss["iss_position"]["longitude"])

    if latitude-5 <=latitude_iss <= latitude+5 and longitude-5 <= longitude_iss <= longitude+5:
        return True
    else:
        return False

def is_night():
    paramenters = {
        "lat" : latitude,
        "lng" : longitude,
        "formatted":0
    }

    response_myposition = requests.get(url="https://api.sunrise-sunset.org/json",params=paramenters)
    response_myposition.raise_for_status()
    data_mylocation = response_myposition.json()
    sunrise =int(data_mylocation['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data_mylocation['results']["sunset"].split("T")[1].split(":")[0])
    to_day = datetime.now().hour

    if to_day > sunset or to_day < sunrise:
        return True
    else:
        return False
while True:
    time.sleep(60)
    if is_night() and Iss_location():
        my_email = "songponsosoxx@gmail.com"
        my_password = "mhvrevylgezzeghd"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connections:
            connections.login(user=my_email,password=my_password)
            connections.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:LOOK AT THIS THE ISS IS ABROVE US!!\n\nJUST LOOK AT IT FUCK"
            )

    else:
        print("NOTING DON't CARE ABOUT IT")
