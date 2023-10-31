import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "rzmobiledev@gmail.com"
MY_SMTP = "smtp.gmail.com"
MY_PASS = "ucbldzutrdgrxrdd"  # fill with gmail password
MY_LAT = -6.200000
MY_LONG = 106.816666


def is_iss_overhead():
    website = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=website)

    response.raise_for_status()

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the iss position
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude + 5:
        return True


def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    api = "https://api.sunrise-sunset.org/json"

    response = requests.get(api, params=params)
    response.raise_for_status()
    data = response.json()

    time_now = datetime.now().hour

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now >= sunset or time_now <= sunrise:
        return True


# if the iss at close to my current position
# and it's currently dark
# send me an email to tell me to look up
while True:
    time.sleep(60)
    if is_iss_overhead():
        with smtplib.SMTP(host=MY_SMTP, port=587) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASS)
            conn.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="rizal.safril@gmail.com",
                msg=f"Subject:Look Up\n\n"
                    f"The ISS is above you in the sky.")
