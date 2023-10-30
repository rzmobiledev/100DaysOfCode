import smtplib
import datetime as dt
import random

my_email = "rzmobiledev@gmail.com"
other_email = "rizal.safril@gmail.com"
smtp = "smtp.gmail.com"
password = "" # fill with gmail password
#
# with smtplib.SMTP(host=smtp, port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=other_email, msg="Subject:Hello\n\nHello rizal, how are you!")

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP(host=smtp, port=587) as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=other_email,
            msg=f"Subject:Monday Motivation\n\n"
            f"{quote}"
        )
