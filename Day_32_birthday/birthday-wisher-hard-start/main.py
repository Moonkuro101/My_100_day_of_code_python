##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import smtplib
import pandas as pd
import random
import datetime as dt

my_email = "songponsosoxx@gmail.com"
my_password = "mhvrevylgezzeghd"

birthdays_data = pd.read_csv("birthdays.csv")
birthdays_dict={(row['month'],row['day']) : row for index,row in birthdays_data.iterrows()}
today = dt.datetime.now()
date = today.day
month = today.month
try: 
    person = birthdays_dict[(month,date)]
except KeyError:
   print("There is no one in the lists born today.")
else:
    placeholder = "[NAME]"
    if (month,date) in birthdays_dict: 
        for i in range (0,5):
            rn = random.randint(1,3)
            with open(f".\letter_templates\letter_{rn}.txt") as file:
                details = file.read()
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                the_letter = details.replace(placeholder,person["name"])
                connection.sendmail(from_addr=my_email,to_addrs=birthdays_dict[(month,date)]["email"],msg=f"Subject:Mam I Earth Letter\n\n{the_letter}")
                print("the mail have sent sucessful")




