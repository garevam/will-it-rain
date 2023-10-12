from openmeteo_py import OWmanager
from openmeteo_py.Hourly.HourlyHistorical import HourlyHistorical
from openmeteo_py.Daily.DailyHistorical import DailyHistorical
from openmeteo_py.Options.HistoricalOptions import HistoricalOptions
from openmeteo_py.Utils.constants import *

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
    # Latitude, Longitude
    longitude = 33.89
    latitude = -6.31

    hourly = HourlyHistorical()
    daily = DailyHistorical()
    options = HistoricalOptions(latitude, longitude, nan, False, celsius, kmh, mm, iso8601, utc, "2022-12-31",
                                "2023-02-26")

    # notice that we had to give the value "None" for the hourly parameter,otherwise you'll be filling the hourly parameter instead of the daily one.
    mgr = OWmanager(options, OWmanager.historical, hourly.all(), daily.all())

    # Download data,here we want it as a key value json where the keys are dates and values the corresponding values of that date (technically timestamp)
    meteo = mgr.get_data(1)

    print(meteo)

if __name__ == '__main__':
    main()
