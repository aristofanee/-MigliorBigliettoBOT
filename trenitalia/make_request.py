import request_function
import json
import requests




url_request = "https://www.lefrecce.it/Channels.Website.BFF.WEB/website/ticket/solutions"


def create_request(city_in, city_out, limit, delta_days = 0, delta_h = 0):
    with open("request_template.json", "r") as file:
        request_json = json.load(file)

    request_json["departureLocationId"] = request_function.search_station(city_in)[0]
    request_json["arrivalLocationId"] = request_function.search_station(city_out)[0]
    request_json["departureTime"] = request_function.handle_date(delta_days, delta_h)
    request_json["criteria"]["limit"] = limit

    #print(request_json)

    response = requests.post(url_request, json=request_json)


    if response.status_code == 200:
    # Request was successful
        #print("\nRequest was successful!")
        text = response.text
    
        #with open('output_solutions.json', 'w') as file:
            #file.write(text)
        #print(type(text))
        return text
    else:
    # Request failed
        print(f"\nRequest failed with status code: {response.status_code}")


#everything in GRIDS is useless!!!!!!!!!!!!!!!
#create_request("milano", "firenze", 1000)


