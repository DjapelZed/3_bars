import codecs
import json
import shutil
import math


def load_data(filepath):
    shutil.copy2(filepath, 'json-txt.txt')
    open_json = codecs.open('json-txt.txt', 'r', 'cp1251')
    json_to_parse = json.loads(open_json.read())
    return json_to_parse


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return print('Biggest bar is: ', biggest_bar['Name'], '-', biggest_bar['SeatsCount'])


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return print('Smallest bar is: ', smallest_bar['Name'], '-', smallest_bar['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    closet_bar = min(data, key=lambda x: math.sqrt
    ((x['geoData']['coordinates'][0] - longitude) ** 2 +
     (x['geoData']['coordinates'][1] - latitude) ** 2))
    return print('Closet bar is: ', closet_bar['Name'])


if __name__ == '__main__':
    filepath = input('Enter file path: ')
    get_biggest_bar(load_data(filepath))
    get_smallest_bar(load_data(filepath))
    get_closest_bar(load_data(filepath), float(input('Longitude: ')), float(input('Latitude: ')))
