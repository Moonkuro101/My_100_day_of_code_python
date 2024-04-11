import requests
from flight_data import FlightData
from pprint import pprint
kiwi_endpoint = "https://api.tequila.kiwi.com"
auth_token = "JidHBvtaYmXxgb8aeo-EcVbxqb3RTpZm"


class FlightSearch:
    def get_destination_code(self,city_name):
        location_endpoint = f"{kiwi_endpoint}/locations/query"
        headers = {"apikey": auth_token}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    
    def get_data_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey" : auth_token}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "THB"
        }
        response = requests.get(
            url=f"{kiwi_endpoint}/v2/search",
            headers=header,
            params=query,
        )
        try:
            
            data = response.json()["data"][0]



        except IndexError:
            print(f"No direct flights found for {destination_city_code}.")
            try:
                query["max_stopovers"] = 1
                response = requests.get(
                url=f"{kiwi_endpoint}/v2/search",
                headers=header,
                params=query,
                )

                data = response.json()["data"][0]
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                
                return flight_data
            except:
                print(f"No any flights found for {destination_city_code}.")
                return None
        
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: THB{flight_data.price}")
            
            return flight_data
        