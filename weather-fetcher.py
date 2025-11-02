import requests
response = requests.get("https://wttr.in/?format=3")
print("Weather:", response.text)
