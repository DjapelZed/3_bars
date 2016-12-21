import codecs
import json
import math


def load_data(filepath):
    with codecs.open(filepath, 'r', 'cp1251') as json_to_parse:
        json_to_parse = json.loads(json_to_parse.read())
    return json_to_parse


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return biggest_bar, biggest_bar


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return smallest_bar, smallest_bar


def get_closest_bar(data, longitude, latitude):
    closet_bar = min(data, key=lambda x: math.sqrt
    ((x['geoData']['coordinates'][0] - longitude) ** 2 +
     (x['geoData']['coordinates'][1] - latitude) ** 2))
    return closet_bar


if __name__ == '__main__':
    filepath = input('Enter file path: ')
    json_file = load_data(filepath)
    biggest_bar = get_biggest_bar(json_file)
    smallest_bar = get_smallest_bar(json_file)
    closest_bar = get_closest_bar(json_file, float(input('Longitude: ')), float(input('Latitude: ')))
    print('Biggest bar is', biggest_bar[0]['Name'],':',biggest_bar[1]['SeatsCount'])
    print('Smallest bar is', smallest_bar[0]['Name'], ':', smallest_bar[1]['SeatsCount'])
    print('Closet bar is', closest_bar['Name'])

