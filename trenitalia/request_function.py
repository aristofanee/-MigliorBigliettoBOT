import urllib.request
import json
from datetime import datetime, timedelta, date
import pytz

def search_station(city_name):

    base_url = "https://www.lefrecce.it/Channels.Website.BFF.WEB/website/locations/search?name="

    #number of stations searched per request, it's 2 otherwise it does not work
    n_limit = 2
    url_limit = "&limit=" + str(n_limit)

    url = base_url + city_name + url_limit
    page = urllib.request.urlopen(url)
    json_string = page.read().decode("utf-8")

    id = [json.loads(json_string)[i]["id"] for i in range(n_limit) if json.loads(json_string)[i]["id"] != None]

    #if type(id[0] is int):
        #print(json_string)
        #print("\n")
    return id

def handle_date(amnt_days,amnt_hours):

    # Define a date
    start_date = datetime.now(pytz.timezone('Etc/GMT-2'))

    # Add 5 days to the date
    new_date = start_date + timedelta(days=amnt_days,hours=amnt_hours)

    formatted_date = new_date.isoformat()[:-9] + new_date.isoformat()[-6:]

    #return "2024-04-07T15:00:00.000+02:00"
    #print(formatted_date)
    return formatted_date
    



#print(search_station("milano"))
#print(search_station("firenze"))
#print(handle_date(7,2))
