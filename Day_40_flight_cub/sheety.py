import requests

end_point_sheety = "https://api.sheety.co/7b531558897c8ea66ebda08cb5bcf809/searchFlight/users"


def post_new_row(first_name,last_name,email):

    if check_user(email=email):
        print('You already in club')

    else:
        body = {
            "user" : {
                "firstName" : first_name,
                'lastName' : last_name,
                'email':email
            }
        }
        reponse = requests.post(url=end_point_sheety,json=body)
        print(reponse.text)
        print("You sucessful to be in our club look forward")


def check_user(email):
    response_get = requests.get(url=end_point_sheety)
    data_sheet = response_get.json()
    for user in data_sheet['users']:
        if user['email'] == email:
            return True

