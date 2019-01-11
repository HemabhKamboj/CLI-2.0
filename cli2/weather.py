#!/home/hkamboj/CLI_custom_features/venv/bin/python3


"""The program retireves Location from IP addrress and then displays weather of user's current location,
prompts the user to know weather of any other city.
"""

import requests
from pprint import pprint
from urllib.request import urlopen


def internet_on():
    """ Checks for internet Connection, by checking availability of google.com.
        The function will return false  (after waiting for 2 seconds) in any case google.com 
        is not accessible.

        Args: 
            Nil

        Returns: 
            Boolean
            True: If internet connectivity is available.
            False: If internet connectivity is not available.

     """   
    try:
        urlopen('http://www.google.com', timeout=2)
        return True
    except urlopen.URLError as err: 
        return False

def GetLocation():
    """ Gets user's current location coordinates by IP Address.
        May provide innacurate information in case of VPN.
        
        Args:
            Nil
        
        Returns: Location in type str.  "lat="+Latitude+"&lon="+Longitude
                """
    IPinfoRequest = requests.get('https://ipinfo.io/')
    IPinfo = IPinfoRequest.json()
    Location = IPinfo['loc'].split(',')
    Latitude = Location[0]
    Longitude = Location[1]
    LocationForOpenweather = "lat="+Latitude+"&lon="+Longitude
    return(LocationForOpenweather)
    
def GetCity():
    """ Gets user's current city by IP Address.
        May provide innacurate information in case of VPN.
        
        Args:
            Nil
        
        Returns: City name in type str.  
    """
    IPinfoRequest = requests.get('https://ipinfo.io/')
    IPinfo = IPinfoRequest.json()
    City = IPinfo['city']
    return(City)
         

def GetWeatherByLocation():
    """ Calls and retrieves user location from GetLocation () then,
        Calls openweather api and fetches weather info.

        Args:
            Nil

        Returns:
                Temperature in type int.
                Humidity in tyoe int.
                Description in tyoe str.    
    """
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
    print(type(Humidity))
    return(Temp, Humidity, Description)


def GetWeatherByCity(City):
    """Calls openweather api and fetches weather info.
        Checks for invalid city name passed.

        Args:
            City

        Returns:
                Temperature in type int.
                Humidity in tyoe int.
                Description in tyoe str.    
    """
    WeatherUrl = "http://api.openweathermap.org/data/2.5/weather?q="+ City + "&appid=b4bacbe2dc824431289800439f1ec3df&units=metric"    
    WeatherRequest = requests.get(WeatherUrl)
    WeatherInfo = WeatherRequest.json()
    if ('main' in WeatherInfo):
        pass
    else:
        print("Invalid City Name")
        exit()    
    Temp = WeatherInfo['main']['temp']
    Humidity = WeatherInfo['main']['humidity']
    Description = WeatherInfo['weather'][0]['description']
    return(Temp, Humidity, Description)

def PrintWeather(Weather):
    """ Prints weather info a concise and simple way.

        Args:
            Weather

        Returns:
            1
    """
    print('Temperature : {}°C'.format(Weather[0]))
    print('Humidity :  {} %'.format(Weather[1]))
    print('Description : {}'.format(Weather[2])+'\n')
    return 1


def GetCityByUser():
    """Prompts user to enter to enter City and calls PrintWeather()

        Args:
            Nil

        Returns:
            1    
    """
    City = str(input())
    if (City == ""):
        exit()
    Weather = GetWeatherByCity(City)
    print("The weather in " + City + " is:\n")
    PrintWeather(Weather)  
    return 1  



def main():
    """ Main function of the program.
        First calls internet_on() for checking internet connection exits the console if retrieved False,
        then  calls GetCity() for retrieving user's current city and prints hello statement
        Calls GetWeatherByLocation(). 
        The location in coordinates is again retrieved by GetWeatherByLocation() to have precise location rather
        than city name.
        Then weather info retrieved is passed to Printweather().
        Finally, prompts user to know weather of other city

        Args:
            Nil

        Returns:
            1

    """
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
    return 1


if (__name__ == "__main__"):
    main()