import smtplib
import datetime as dt
from random import choice
my_email = "ton2425856359@gmail.com"
my_password = "xjpvghchwatdheeo"
now = dt.datetime.now()
weak_day = now.weekday()
if weak_day == 5:
    with open("quotes.txt","r") as quotesfile:
        quotes = quotesfile.readlines()
        quote = choice(quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # Adjust port and timeout
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Monday Motivation\n\n{quote}")

        print("Email sent successfully!")


