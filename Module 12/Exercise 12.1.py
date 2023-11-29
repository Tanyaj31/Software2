import requests

request = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(request)
    if response.status_code == 200:       #to check if the request was successful (status code 200)
        json_response = response.json()    #parsing the JSON response
        print(json_response["value"])      #printing the joke text

except requests.exceptions.RequestException as e:
    print("Sorry, but the request could not be completed.")