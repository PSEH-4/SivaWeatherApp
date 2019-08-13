import requests

def getAPIResponse():
    api_url = 'https://samples.openweathermap.org/data/2.5/forecast?q='
    api_city = 'London,us'
    api_key = 'b6907d289e10d714a6e88b30761fae22'
    api_str = api_url + api_city + '&appid=' + api_key
    response = requests.get(api_str)
    print response.text
    return response.text