import json
from urllib.request import urlopen
import requests

TODOIST_TOKEN = '36f6c9e6a726745cc2c9a54c8ca751eeefd11904'

DARKSKY_API_KEY = 'd8aa09ea38d58885d977f000c2330a1f'
DARKSKY_LAT = '1.3236'
DARKSKY_LONG = '103.9273'
DARKSKY_LOCATION = 'Bedok'

ALADHAN_LATITUDE = 0
ALADHAN_LONGITUDE = 0
ALADHAN_TIMEZONE = 0
ALADHAN_METHOD = 0

todolist_items = 0;


def test():
    f = requests.get('https://api.darksky.net/forecast/' + DARKSKY_API_KEY + '/' + DARKSKY_LAT + ',' + DARKSKY_LONG + '?units=si')
    # print(json_string)
    parsed_json = f.json()
    # print(parsed_json)
    location = DARKSKY_LOCATION
    temp_c = parsed_json['currently']['temperature']
    icon = parsed_json['currently']['icon']
    weather = parsed_json['currently']['summary']
    print("Current temperature in %s is: %s with weather of %s" % (location, temp_c, weather))
    icons_list = {u'chancerain': u'', u'chancesleet': u'', 'chancesnow': u'', 'chancetstorms': u'', 'clear': u'',
                  'flurries': u'', 'fog': u'', 'hazy': u'', 'mostlycloudy': u'', 'mostlysunny': u'',
                  'partlycloudy': u'', 'partlysunny': u'', 'sleet': u'', 'rain': u'', 'sunny': u'',
                  'tstorms': u'', 'cloudy': u''}
    f.close()

if __name__ == '__main__':
    test()