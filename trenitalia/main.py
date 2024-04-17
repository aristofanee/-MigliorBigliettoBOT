import json
import urllib.request
import requests



url_info = "https://www.lefrecce.it/Channels.Website.BFF.WEB/website/ticket/solutions"

data_json = open("test.json", "r")
data = json.load(data_json)
data_json.close()




response = requests.post(url_info, json=data)

if response.status_code == 200:
    # Request was successful
    print("Request was successful!")
    text = response.text
    
    with open('output_solutions.json', 'w') as file:
        file.write(text)
       

else:
    # Request failed
    print(f"Request failed with status code: {response.status_code}")