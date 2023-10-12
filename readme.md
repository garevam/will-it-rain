# will-it-rain

This program is to be the backbone of a little web service. It should take a location and a date range and access
open-meteo's API to retrieve the last 50 years of weather data for that location and date range. Then, it will provide
information to a dashboard to present the user some statistics:
-average precipitation pattern over the average year,
-average yearly precipitation pattern from 1970-1975 compared to 2017-2022,
-a graph showing the amount of precipitation every year on that specific date range and finally
-a simple % chance of rain for the desired date in a future year

This program's predictions are not to be taken seriously. Weather patterns are highly irregular and everchanging -
specially in these days of accelerated climate change.

This software or I are not in any way associated with or part of open-meteo.

### openmeteopy

openmeteopy is a third party wrapper under the license, textually citing, *DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE*.
I am uploading this code to my own repository so that (hopefully) the whole thing will work in the end, without me having
to provide my own API key.
Here's the source: https://github.com/m0rp43us/openmeteopy

### To do

- User input
- Data retrieval and manipulation
- Data presentation
- Possibly an illustration of the issue with weather data resolution (rain falls in the mountains behind the city, not in the city, etc.)

### How does it work?

The plan is to avoid needing my own API key by using the openmeteopy wrapper (https://github.com/m0rp43us/openmeteopy).
This removes the multiple unnecessary complications and potential costs from what is just a practice and display piece.
Using this wrapper, we can retrieve the required data from open-meteo's historical weather database in JSON format.
Finally, we can shape it up as needed and then present it to the user, which will require some assistance from front
end languages - but I'll cross that bridge when I get there.

### Requirements

This should be set up to run online, easily reachable by users, but running the code should require

- Python 3.11
- openmeteopy (https://github.com/m0rp43us/openmeteopy)

### Limitations

**On the reliability of weather data:** Weather prediction is a very complicated thing, and even the most stable weather
patterns are highly irregular, or can experience temporal irregularities. open-meteo gets its data from multiple official,
high quality sources, but the weather data itself can never be too precise. According to their own disclaimer, weather
data is gathered with a resolution between 1,5 and 11 kilometers. This means that, in the areas with lower resolution,
rain fallen up to 11 km away from the city whose weather we are checking will still be counted as rain fallen on that
city. Ultimately, this program is no more than a little curiosity.

This program was originally planned to provide a wide array of weather data and predictions, but the scope of the project
and the complexity of the required code increased rapidly. To better fulfill the program's purpose, which is both to
practice and to create a little display piece that is functional and immediately usable over the browser, I chose to
severely limit functionality to the bare minimum: precipitation (meaning the combination of rain and snow).

This program uses someone else's generously provided access key, and should be used with moderation and in no case for
any sort of commercial purposes.

### Future development possibilities

- Save the session
- Remember multiple queries within the same session, to compare them without having to query open-meteo repeatedly
- Some sort of comparison function to overlay the graphs for different cities/dates
- Offer to save a screenshot of the currently displayed data
- Build and host my own backed with my own API key instead of relying on the third party openmeteopy wrapper

## Personal aspects

### Challenges

Finding a way to access the required data has been complicated. There's many historic weather databases, but few can be
accessed at least partially for free. The best candidates, open-meteo and openweathermap, also have their complications:
open-meteo offers their own browser API for end users, but no API to programmatically access all the data. openweatherapp
requires a subscription and using my own API key: for security, this shouldn't be openly available, but I also don't want
to force the end user to provide their own API key. This would force me to build a back end server, quickly increasing
the complexity of the project beyond its current desired scope. Fortunately, openmeteopy seems to help me avoid both issues.

### What did I learn?

So far the focus has been on program design and scope control.
