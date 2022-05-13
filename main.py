import requests
import smtplib
import os
EMAIL = os.environ.get("MAIL_ID")

PASSWORD = os.environ.get("PASSWORD")
APP_ID = os.environ.get("APP_ID")
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=EMAIL,
                 password=PASSWORD)

#TO MAKE IT MORE EFFICIENT INPUT DICTIONARY CONTAINING LOCATION AND GEOGRAPHICAL MEASUREMENTS

MY_LAT,MY_LONG = (19.232389,73.087761)  #location:Mumbai
parameters = {"lat":MY_LAT, "lon":MY_LONG,
              "appid": APP_ID,
              "exclude":"current,minutely,daily"}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data = response.json()

for items in data["hourly"][0:13]:
    weather_id = items["weather"][0]["id"]
    #print(weather_id)
    if weather_id < 700:
        will_rain = True
        print(items)
    else:
        will_rain=False
if will_rain:
    connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL ,msg=f"Subject:Rain alert\n\nTake a umbrella")
    connection.close()
    #print("bring a umbrella")
    print(items["temp"])
#print(data["hourly"][0]["weather"][0]["id"])



