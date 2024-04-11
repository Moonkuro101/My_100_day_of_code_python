import requests

end_point_sheety = "https://api.sheety.co/7b531558897c8ea66ebda08cb5bcf809/searchFlight/prices"

class DataManager:
    def __init__(self) :
        self.destination = {}
    
    def get_data(self):
        response = requests.get(url=end_point_sheety)
        data = response.json()['prices']
        self.destination = data
        return self.destination
    
    def update_destination_code(self):
        for city in self.destination:
            new_data = {
                "price" : {
                    'iataCode' : city['iataCode']
                }
            }
            response = requests.put(url=f"{end_point_sheety}/{city['id']}",json=new_data)
            print(response.text)