from openmeteo_py import OWmanager
from openmeteo_py.Daily.DailyHistorical import DailyHistorical
from openmeteo_py.Options.HistoricalOptions import HistoricalOptions
from openmeteo_py.Utils.constants import *  # necessary by the wrapper to interpret the options correctly

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


def main():
    # To do: Latitude, Longitude to be user input
    longitude = 33.89
    latitude = 26.31

    # To do: add an input setting for the dates, which are right now hard coded in "options = HistoricalOptions(xxx)"

#    hourly = HourlyHistorical()
    weatherquery = DailyHistorical().precipitation_sum()
    options = HistoricalOptions(  # All are required by the wrapper. Removing any, even if not used, will cause a crash
        latitude,
        longitude,
        nan,  # required by wrapper to interpret options correctly
        False,  # don't include current weather
        celsius,  # temperature unit
        kmh,  # wind speed unit
        mm,  # precipitation unit
        iso8601,  # time format
        utc,  # timezone
        "2022-01-01",  # start date
        "2022-01-02"  # end date. Note: this day will NOT be included in the query!
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

    # To do: flatten that "dictionary in a dictionary" into a simple dictionary

if __name__ == '__main__':
    main()
