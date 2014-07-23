from datetime import datetime
import logging

import requests

from lxml import etree

logger = logging.getLogger(__name__)

def _parse_station(xml_element):
    '''
    Parses out the station data and and returns a dictionary
    of station data.
    '''
    station = {}

    for child in xml_element.getchildren():

        if 'observation_time' in child.tag:
            station[child.tag] = _parse_observation_time_string(child.text)
        else:
            station[child.tag] = child.text

    return station

def _parse_observation_time_string(time_string):
    '''
    Parses observation timestring, returns isodate
    '''
    # first try normal format
    # Last Updated on Jul 5 2014, 4:55 pm PDT
    try:
        d = datetime.strptime(time_string, 'Last Updated on %b %m %Y, %H:%M %p %Z')
    except:
        d = None

    # try other format
    # Sat, 05 Jul 2014 16:55:00 -0700
    if not d:
        try:
            d = datetime.strptime(time_string, '%a, %m %b %Y %H:%M:%S %z')
        except:
            d = None

    result = None
    if d:
        result = d.isoformat()

    return result

def _get_stations():
    '''
    returns list of xml station objects
    '''
    logger.debug('downloading stations')
    r = requests.get('http://w1.weather.gov/xml/current_obs/index.xml')

    #remove xml declaration
    index = r.text.find('>')

    # parse xml
    xml = etree.fromstring(r.text[index+1:])

    return xml.xpath('//station')

def get_stations():
    '''
    returns a list of station dictionary objects
    '''
    # download urls
    

    stations = _get_stations()
    logger.debug('%s stations downloaded.' % repr(len(stations)))

    station_dicts = []

    logger.debug('parsing stations')

    for station in stations:
        station_dict = _parse_station(station)
        station_dicts.append(station_dict)
    return station_dicts
    
