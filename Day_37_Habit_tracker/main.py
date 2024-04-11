import requests
import datetime as dt
usernname="songpon"
auth_token = "siht-si-eht-authentication"
graph_ID = "graph1"
pixela_params = {
    "token":auth_token,
    "username":usernname,
    "agreeTermsOfService":'yes',
    "notMinor":'yes'
}
pixela_endpoin = "https://pixe.la/v1/users"

# respons = requests.post(url=pixela_endpoin,json=pixela_params)

graph_endpoin = f"{pixela_endpoin}/{usernname}/graphs"

graph_params = {
    "id":"graph1",
    "name":"My_coding",
    "unit":"Hours",
    "type":"float",
    "color":"momiji",
}

header={
    "X-USER-TOKEN": auth_token,
}

response = requests.post(url=graph_endpoin,json=graph_params,headers=header)


today = dt.datetime(year=2024,month=3,day=31)
todays = today.strftime("%Y%m%d")



# add_splot = {
#     "date":todays,
#     "quantity": "5"
# }

update_splot = {
    "quantity" : "20"
}


graph_add = f"{graph_endpoin}/{graph_ID}"
graph_update = f"{graph_add}/{todays}"
print(graph_update)

print(todays)

response = requests.delete(url=graph_update,headers=header)
print(response.text)


# print(respons.text)
# print(respons.json)