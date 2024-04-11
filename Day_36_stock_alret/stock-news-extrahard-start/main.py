import requests
from twilio.rest import Client
import json
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
endpoin_stock = "https://www.alphavantage.co/query"
parameter = {
"function" :"TIME_SERIES_DAILY",
"symbol":STOCK,
"apikey":"JZHJVYWER62SZAWI" 
}
respones_stock = requests.get(url=endpoin_stock,params=parameter)
respones_stock.raise_for_status()

data = respones_stock.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]

yesterday_data = data_list[0]
yesterday_close_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_close_price)-float(day_before_yesterday_close_price)
up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

difference_percentage = round((difference/float(yesterday_close_price))*100)

if difference_percentage > -10:
    print("ihavesent you something")
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    parameter_news = {
    'q':COMPANY_NAME,
    "language":"en",
    "sortBy":"publishedAt",
    "apikey":"6c27eb78f44e41e5a9a431dc20713bab"
    }
    endpoin_news = "https://newsapi.org/v2/everything"

    respones_news = requests.get(url=endpoin_news,params=parameter_news)
    data_news = respones_news.json()["articles"]
    news_3 = data_news[:4]
    format_article = [f"{STOCK} : {up_down}{difference_percentage}%\nHeadline {aritcle['title']}\nBrief {aritcle['description']}" for aritcle in news_3]
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 

    account_sid = 'ACc34ace9eee48683bbee342d8088d28b1'
    auth_token = '37ed51c2ab6e18490eb7c3a086efb58b'
    client = Client(account_sid, auth_token)
    for article in format_article:
        message = client.messages.create(
        from_='+12568418392',
        body=article,
        to='+66630488856'
        )

    print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

