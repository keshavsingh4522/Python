# !pip3 install phonenumbers
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
phone_number=phonenumbers.parse(input('Enter phone numbers with coutry code: '))
# this will print the country name
print(geocoder.description_for_valid_number(phone_number,'en'))
#this will print the  service provider name
print(carrier.name_for_valid_number(phone_number,'en'))