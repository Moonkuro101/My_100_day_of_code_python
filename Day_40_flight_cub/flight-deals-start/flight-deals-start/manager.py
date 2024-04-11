import requests

end_point_sheety = "https://api.sheety.co/7b531558897c8ea66ebda08cb5bcf809/searchFlight/users"

def get_users_email():
    response = requests.get(url=end_point_sheety)
    data_sheet = response.json()["users"]
    emails = [user['email'] for user in data_sheet]
    return emails

