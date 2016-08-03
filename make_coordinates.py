# John Loeber | Python 2.7.6 | contact@johnloeber.com | August 3 2016

from Credentials.addresses import start_address, end_address
from pygeocoder import Geocoder

start_latitude, start_longitude = Geocoder.geocode(start_address).coordinates
end_latitude, end_longitude = Geocoder.geocode(start_address).coordinates

# we write this information to a file so we don't have to query the google maps
# api every time we run the script.

with open("Credentials/coordinates.py","w") as f:
    f.write('start_latitude = ' + str(start_latitude) + '\n')
    f.write('start_longitude = ' + str(start_longitude) + '\n\n')
    f.write('end_latitude = ' + str(end_latitude) + '\n')
    f.write('end_longitude = ' + str(end_longitude))
