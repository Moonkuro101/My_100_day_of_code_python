from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from manager import get_users_email
from notification_manager import NotificationManager
import smtplib
from pprint import pprint

my_email = "ton2425856359@gmail.com"
my_password = "xjpvghchwatdheeo"


data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "BKK"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination = sheet_data
    data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))



for destination in sheet_data:
    flight = flight_search.get_data_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    
    if flight is None:
        continue

    if destination['lowestPriceThb'] > flight.price:
        message= f"Low price alert! Only THB{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        if flight.max_stopover > 0:
            message += f"\nFlight has {flight.max_stopover} stop over, via {flight.via_city}."
            print(message)
        user_email = get_users_email()

        for email in user_email:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email,password=my_password)
                    connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject:Deal Flight club!!\n\n{message}")
                    print("the mail have sent sucessful")

        
            




