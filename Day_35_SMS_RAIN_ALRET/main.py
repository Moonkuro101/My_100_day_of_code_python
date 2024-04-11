import requests
import json
from twilio.rest import Client

parameters = {
    "q": "Bang Bua Thong,Thailand",
    "cnt":4,
    "appid": "cb7230bb67653c7149b92908195d58b4"
}
account_sid = 'ACc34ace9eee48683bbee342d8088d28b1'
auth_token = '37ed51c2ab6e18490eb7c3a086efb58b'
client = Client(account_sid, auth_token)

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)

# Check if the request was successful
if response.status_code == 200:
    data_api = response.json()
    with open("/weather_data.json", "w") as json_file:
        json.dump(data_api, json_file)
    print("JSON data saved to 'weather_data.json'")
    # Now you can work with the data_api dictionary
    # print(data_api)

def bring_umberral(data_api):
    Bring_or_not = False
    the_weather = [ weather_H3["weather"][0]["id"] for weather_H3 in data_api["list"]]
    
    for i in the_weather:
        if i <=700:
            Bring_or_not = True
    
    if Bring_or_not:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="it's going to rain today ☂️",
            from_='+12568418392',
            to='+660630488856'
        )
        print(message.status)

    else :
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body="Just a usual day make it fun for you ☀️" ,
        from_='+12568418392',
        to='+660630488856'
        )
        print(message.status)

bring_umberral(data_api=data_api)