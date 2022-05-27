## Earthquake App
The app using free api [Earthquake Catalog](https://earthquake.usgs.gov/fdsnws/event/1/), requests and geopy libs.
The app is designed to be launched from the terminal. To do this, you need to make the `earthquake_app.py` executable.

Usage
```-h # for info
earthquake_app CITY_NAME -r RADIUS of earthquake search (1000 km by default)

#------------

earthquake_app pekin
There are 2 earthquakes at 23:11:26 in Pekin by coordinates 39.906217:116.3912757 on a radius of 1000 kilometers

earthquake_app denpasar -r 350
There are 3 earthquakes at 23:13:40 in Denpasar by coordinates -8.6524973:115.2191175 on a radius of 350 kilometers
