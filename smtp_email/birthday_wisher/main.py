import smtplib
import random
import pandas as pd
import datetime as dt


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

df = pd.read_csv("birthdays.csv")
df_to_list = df.to_dict(orient="records")
# [{'name': 'rizal', 'email': 'rizal.safril@gmail.com', 'year': 1984.0, 'month': 10.0, 'day': 30.0}]


def send_email(**kwargs: dict):
    my_email = "rzmobiledev@gmail.com"
    smtp = "smtp.gmail.com"
    password = "" #fill with gmail password

    # pick random template
    templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    random_template = random.choice(templates)

    with open(f"./templates/{random_template}") as letter:
        data = letter.read()
        data_rep = data.replace('[NAME]', kwargs['name'])

    with smtplib.SMTP(host=smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=kwargs['email'],
            msg=f"Subject:Happy Birthday {kwargs['name']}\n\n"
            f"{data_rep}"
        )


now = dt.datetime.now()
month = now.month
date = now.day

for person in df_to_list:
    if month == person['month'] and date == person['day']:
        send_email(email=person['email'], name=person['name'])

