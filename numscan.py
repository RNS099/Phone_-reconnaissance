import requests
from geopy.geocoders import Nominatim

def get_details(phno):

    key = "your numlookup api key"
    if phno :
        url = f"https://api.numlookupapi.com/v1/validate/{phno}?apikey={key}"
        #headers = { "apikey" : key}

        response = requests.get(url)
        json_data = response.json()

        if 'message' not in json_data:

            loc = Nominatim(user_agent="GETLOC")
            getLoc = loc.geocode(json_data["location"])

            json_data ["coordinates"] = (getLoc.latitude, getLoc.longitude)

        else:
            pass

        return json_data 

            

if __name__ == '__main__':
    number = input("Enter mobile number with country code: ")
    details = get_details(number)

    for k,v in details.items():
        print(k, v)
        
    


    


