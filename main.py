##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "codelearner5582@gmail.com"
password = "lamxgcjapocohtfa"

# 1. Update the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
df = pd.read_csv("birthdays.csv")
data = df.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
for i in data:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if i["day"] == day and i["month"] == month:
        with open(f"{random.choice(letter_templates)}", "r") as f:
            file_data = f.read()
        new_data = file_data.replace("[NAME]", i["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=i["email"], msg=f"Subject:Happy Birthday\n\n{new_data}")
