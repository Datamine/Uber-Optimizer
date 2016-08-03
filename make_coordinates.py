# John Loeber | Python 2.7.6 | contact@johnloeber.com | August 3 2016

from Credentials.addresses import start_address, end_address
from pygeocoder import Geocoder

start_address_coords = Geocoder.geocode(start_address).coordinates
end_address_coords = Geocoder.geocode(start_address).coordinates
