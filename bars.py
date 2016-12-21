import codecs
import json
import math


def load_data(filepath):
    with codecs.open(filepath, 'r', 'cp1251') as json_to_parse:
        json_to_parse = json.loads(json_to_parse.read())
    return json_to_parse


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return biggest_bar['Name'], biggest_bar['SeatsCount']


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return smallest_bar['Name'], smallest_bar['SeatsCount']


def get_closest_bar(data, longitude, latitude):
    closet_bar = min(data, key=lambda x: math.sqrt
    ((x['geoData']['coordinates'][0] - longitude) ** 2 +
     (x['geoData']['coordinates'][1] - latitude) ** 2))
    return closet_bar['Name']


if __name__ == '__main__':
    filepath = input('Enter file path: ')
    data = load_data(filepath)
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    closest_bar = get_closest_bar(data, float(input('Longitude: ')), float(input('Latitude: ')))
    print(r'Biggest bar is', biggest_bar[0],':',biggest_bar[1])
    print(r'Smallest bar is', smallest_bar[0], ':', smallest_bar[1])
    print(r'Closet bar is', closest_bar)

