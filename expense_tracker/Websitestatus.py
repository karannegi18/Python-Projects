import requests
url = input("enter the url: ")

try:
     response = requests.get(url,
                             timeout=5)
     if response.status_code == 200:
          print("the webisite is working: up")
     else:
          print("the webisite eis working: down")
          
except requests.exceptions.RequestException:
 print("website is down:")          