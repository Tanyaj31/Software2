import requests
import json

city_name = input("Enter your city here: ")
api_key = "3126ec2e567f797e5e170ef5b331fb86"

request = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        kelvin_temperature = json_response["main"]["temp"]
        celsius_temperature = float(kelvin_temperature) - 273.15
        print(round(celsius_temperature, 2))

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")