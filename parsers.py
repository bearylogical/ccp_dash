
import requests
import datetime
import math
from collections import OrderedDict
import pytz

class SGBusParser:
    def __init__(self, acc_key):
        self.AccountKey = acc_key

    def get_timings(self, BusStopID):
        uri = 'http://datamall2.mytransport.sg/'  # Resource URL
        path = 'ltaodataservice/BusArrivalv2?'

        headers = {'AccountKey': self.AccountKey,
                   "accept": "application/JSON"}

        url = uri + path
        payload = ('BusStopCode=' + BusStopID)
        j = requests.get(url, headers=headers, params=payload).json()

        busArr = j['Services']
        now = datetime.datetime.now(tz=pytz.timezone("Asia/Singapore"))
        fmt = "%Y-%m-%dT%H:%M:%S%z"

        arrival = []

        for index in range(len(busArr)):
            arrivalTemplate = OrderedDict({
                'Bus': ' ',
                'Data':
                    [
                        {
                            'NextBus':
                                [
                                    {
                                        'ArrivalTime':'',
                                        'Latitude':'',
                                        'Longitude':''
                                    }
                                ],
                            'NextBus2':
                                [
                                    {
                                        'ArrivalTime': '',
                                        'Latitude': '',
                                        'Longitude': ''
                                    }
                                ],

                            'NextBus3':
                                [
                                    {
                                        'ArrivalTime': '',
                                        'Latitude': '',
                                        'Longitude': ''
                                    }
                                ],
                        }
                    ]
            })
            arrivalTemplate['Bus'] = (busArr[index]['ServiceNo'])
            ArrivalTimes = sorted((arrivalTemplate['Data'][0]).keys())
            for t in range(len(ArrivalTimes)):
                descKey = ArrivalTimes[t]
                if ((busArr[index][descKey]['Latitude'])):
                    arrivalTemplate['Data'][0][descKey][0]['Latitude'] = busArr[index][descKey]['Latitude']
                    arrivalTemplate['Data'][0][descKey][0]['Longitude'] = busArr[index][descKey]['Longitude']
                else:
                    arrivalTemplate['Data'][0][descKey][0]['Latitude'] = 'N.A.'
                    arrivalTemplate['Data'][0][descKey][0]['Longitude'] = 'N.A.'
                estdArrival = ((busArr[index])[descKey]['EstimatedArrival'])
                if (estdArrival):
                    # get arrival time in secs
                    arrivalInterval = math.trunc((datetime.datetime.strptime(estdArrival, fmt) - now).seconds)
                    if arrivalInterval < 60:
                        (arrivalTemplate['Data'][0][descKey][0]['ArrivalTime']) = 'Arr'
                    else:
                        (arrivalTemplate['Data'][0][descKey][0]['ArrivalTime']) = math.floor(arrivalInterval/ 60)
                else:
                    (arrivalTemplate['Data'][0][descKey][0]['ArrivalTime']) = 'N.A.'
            arrival.insert(index, arrivalTemplate)
        return arrival