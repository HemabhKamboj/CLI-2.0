#!/home/hkamboj/CLI_custom_features/venv/bin/python3


import requests
from pprint import pprint
from urllib.request import urlopen


def internet_on():
    """ Checks for internet Connection, by checking availability of google.com.
        The function will return false  (after waiting for 2 seconds) in any case google.com 
        is not accessible.

        Args: Nil

        Called by : main

     """   
    try:
        urlopen('http://www.google.com', timeout=2)
        return True
    except urlopen.URLError as err: 
        return False

def GetLocation():
    IPinfoRequest = requests.get('https://ipinfo.io/')
    IPinfo = IPinfoRequest.json()
    Location = IPinfo['loc'].split(',')
    Latitude = Location[0]
    Longitude = Location[1]
    LocationForOpenweather = "lat="+Latitude+"&lon="+Longitude
    return(LocationForOpenweather)
    
def GetCity():
    IPinfoRequest = requests.get('https://ipinfo.io/')
    IPinfo = IPinfoRequest.json()
    City = IPinfo['city']
    return(City)
         

def GetWeatherByLocation():
    Location = GetLocation()
    WeatherUrl ="http://api.openweathermap.org/data/2.5/weather?"+ Location +"&appid=b4bacbe2dc824431289800439f1ec3df&units=metric"
    WeatherRequest = requests.get(WeatherUrl)
    WeatherInfo = WeatherRequest.json()
    pprint(WeatherInfo)
    WindSpeed = WeatherInfo['wind']['speed']
    pprint(WindSpeed)
    Temp = WeatherInfo['main']['temp']
    Humidity = WeatherInfo['main']['humidity']
    Description = WeatherInfo['weather'][0]['description']
    return(Temp, Humidity, Description)


def GetWeatherByCity(City):
    WeatherUrl = "http://api.openweathermap.org/data/2.5/weather?q="+ City + "&appid=b4bacbe2dc824431289800439f1ec3df&units=metric"    
    WeatherRequest = requests.get(WeatherUrl)
    WeatherInfo = WeatherRequest.json()
    pprint(WeatherInfo)
    try:
        WindSpeed = WeatherInfo['wind']['speed']
        pprint(WindSpeed)
        pass
    except KeyError as err:
        print("Invalid City name, enter valid city name")
        GetCityByUser()
    Temp = WeatherInfo['main']['temp']
    Humidity = WeatherInfo['main']['humidity']
    Description = WeatherInfo['weather'][0]['description']
    return(Temp, Humidity, Description)



def PrintWeather(Weather):
    print('Temperature : {}°C'.format(Weather[0]))
    print('Humidity :  {} %'.format(Weather[1]))
    print('Description : {}'.format(Weather[2])+'\n')


def main():
    CheckInternet = internet_on()
    if (CheckInternet == True):
        pass
    else:
        print("Cannot connect to internet, Check your connection!")
        exit()    
    CityByLocation = GetCity()
    print("Hello, The weather in your city " + CityByLocation + " is:\n")
    Weather = GetWeatherByLocation()
    PrintWeather(Weather)
    print("To get weather in your any other city, enter city name and press ENTER, to continue just press ENTER")
    GetCityByUser()



def GetCityByUser():
    City = str(input())
    if (City == ""):
        exit()
    Weather = GetWeatherByCity(City)
    print("The weather in " + City + " is:\n")
    PrintWeather(Weather)

    


if (__name__ == "__main__"):
    main()

