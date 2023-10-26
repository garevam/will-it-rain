from openmeteo_py import OWmanager
from openmeteo_py.Daily.DailyHistorical import DailyHistorical
from openmeteo_py.Options.HistoricalOptions import HistoricalOptions
from openmeteo_py.Utils.constants import *  # necessary by the wrapper to interpret the options correctly
from datetime import datetime, timedelta
import re

"""
WIP

This program is to be the backbone of a little web service. It should take a location and a date range and access
open-meteo's API to retrieve the last 50 years of weather data for that location and date range. Then, it will provide
information to a dashboard to present the user some statistics:
-average precipitation pattern over the average year,
-average yearly precipitation pattern from 1970-1975 compared to 2017-2022,
-a graph showing the amount of precipitation every year on that specific date range and finally
-a simple % chance of rain for the desired date in a future year

The dashboard itself is a problem for the future, likely better made with wev dev languages.

Made with Python 3.11
"""


def getdate():
    while True:
        inputstartdate = input("Enter start date (in format yyyy mm dd): ")
        inputenddate = input("Enter end date (in format yyyy mm dd): ")
        daterange = []
        try:
            inputstartdate = datetime.strptime(inputstartdate, "%Y %m %d")
            daterange.append(inputstartdate)
            inputenddate = datetime.strptime(inputenddate, "%Y %m %d")
            inputenddate += timedelta(days=1)  # The meteo database does not include the given end date in the query.
                                               # Adding one day to the user input retrieves the results correctly.
            daterange.append(inputenddate)  # At this point the dates include extra unused data for hours and minutes
            formatted_dates = [date.strftime("%Y-%m-%d") for date in daterange]  # This removes that extra data and
                                                                                 # formats the dates for openmeteo
            return formatted_dates
        except ValueError:
            print("That doesn't seem like a valid date! Did you use the correct format? Try again!\n")


def getcoordinates():
    print("Input here the coordinates of the chosen location. You can easily find the coordinates for any given city in"
          " any search machine like Google.\nThis task might get automatized in the future, but it's a bit complicated"
          " because many cities have the same name!")
    while True:
        print("\nPlease enter the coordinates in format x.x, with up to 4 digits on either side of the dot."
              " Here's some examples:"
              "\nLondon, UK: 51.5072, 0.1276"
              "\nTokyo, Japan: 35.6764, 139.6500"
              "\nNew York, USA: 40.7128, 74.0060"
              "\nNairobi, Kenya: 1.2921, 36.8219")
        longitude = input("Longitude: ")
        latitude = input("Latitude: ")
        pattern = r'^\d{1,4}\.\d{1,4}$'
        if re.match(pattern, longitude) and re.match(pattern, latitude):
            print("These coordinates look valid. Let's hope openmeteo can find them!")
            return longitude, latitude
        else:
            "These coordinates don't seem to match the required format. Try again!"


"""
    In order to keep things simple, the code implemented above uses AAI (Artificial Artificial Intelligence) to identify
    the correct city and it's corresponding coordinates. Some kind of error detection to check whether the input is valid
    coordinates would be nice, though.

    Here's alternative (not tested) code for this function. This should work, but it might struggle finding the correct
    city because many have the same name. "Country" wouldn't be a valid identificator either... There's 67 towns called
    Springfield in the USA.

    from geopy.geocoders import Nominatim
    # Initialize the Nominatim geocoder
    geolocator = Nominatim(user_agent="city-coordinates")
    # Prompt the user for a city name
    city_name = input("Enter a city name: ")
    # Use geocoding to retrieve the coordinates
    location = geolocator.geocode(city_name)
    if location:
        return {location.latitude}, {location.longitude}
    else:
        print(f"Coordinates for {city_name} not found.")
"""


def gethistoricweatherdata(coordinates):
    weatherquery = DailyHistorical().precipitation_sum()
    options = HistoricalOptions(  # All are required by the wrapper. Removing any, even if not used, will cause a crash
        float(coordinates[0]),  # longitude, transformed from string to float so openmeteo can read them
        float(coordinates[1]),  # latitude, also as float for openmeteo
        nan,  # required by wrapper to interpret options correctly
        False,  # don't include current weather
        celsius,  # temperature unit
        kmh,  # wind speed unit
        mm,  # precipitation unit
        iso8601,  # time format
        utc,  # timezone
        "1970-01-01",  # start date
        "2023-01-01"  # end date. Note: this day will NOT be included in the query results!
    )

    # Preparing the for the wrapper. The value "None" fills the hourly parameter, preventing that the daily query is
    # interpreted as an hourly one
    finalquery = OWmanager(options, OWmanager.historical, None, weatherquery)

    # The integer requests different formats for the data:
    # 0 returns a dictionary with some unnecessary data, such as elevation. The last entry is another dictionary, containing YET ANOTHER dictionary with the requested weather data
    # 1 returns just a dictionary containing only the dictionary holding the requested weather data
    # 2 and 3 return some kind of tabular data structure. It seems to be meant for display in a command line
    # Do not change, this code supports specifically the setting 1
    meteodata = finalquery.get_data(1)
    print(meteodata)


def main():
    daterange = getdate()
    coordinates = getcoordinates()
    historicweather = gethistoricweatherdata(coordinates)



if __name__ == '__main__':
    main()
