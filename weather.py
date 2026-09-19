import requests
city = input('ente your city: ')
print("you enter :",city)
API_KEY = "4aaa32d0a457bdd8331b1613cc0796e8"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
print(response.json())