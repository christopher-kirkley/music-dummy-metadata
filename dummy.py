import random

import numpy as np
import pandas as pd

from collections import defaultdict

from faker import Faker
fake = Faker()

catalog_root = 'TR'
number_of_items = 50

class Artists():
    def __init__(self, number_of_artists):
        self.number_of_artists = number_of_artists
        self.artist_list = self.make_artist_list()

    def make_artist_list(self):
        lines = open('./artistnames.txt').read().splitlines()
        artist_list = [random.choice(lines).strip() for name in range(self.number_of_artists)]
        return artist_list

    def random_artist(self):
        artist = random.choice(self.artist_list)
        return artist


class Catalogs():
    def __init__(self, catalog_root, number_of_catalogs, size_va, artist_list):
        self.catalog_root = catalog_root
        self.number_of_catalogs = number_of_catalogs
        self.size_va = size_va
        self.artist_list = artist_list
        self.catalog_artists = self.make_catalog_artists()
        self.catalog_names = self.make_catalog_names()

    def make_catalog_artists(self):
        catalog_artists = self.artist_list[0:self.number_of_catalogs]
        for i in range(self.size_va):
            catalog_artists[i] = 'Various Artists'
        return catalog_artists

    def make_catalog_names(self):
        lines = open('./artistnames.txt').read().splitlines()
        catalog_names = [random.choice(lines).strip() for name in range(len(lines))]
        return catalog_names

    def make_catalog_items(self):
        catalog_items = []
        for i in range(self.number_of_catalogs):
            entry = {'catalog_number': f'{self.catalog_root}-00{i+1}', 
                    'catalog_artist': self.catalog_artists[i],
                    'catalog_name': self.catalog_names[i],
                    }
            catalog_items.append(entry)
        return catalog_items


def random_phrase():
    lines = open('./artistnames.txt').read().splitlines()
    random_phrases = [random.choice(lines).strip() for name in range(len(lines))]
    index = random.randint(1, len(random_phrases))
    random_phrase = random_phrases[index]
    return random_phrase


# def find_unique_catalog_numbers(catalog_df):
#     catalog_numbers = catalog_df['catalog_number'].unique().tolist()
#     return catalog_numbers

def make_track_isrcs(catalog_number):
    tracks_per_catalog = random.randint(2, 10)
    isrcs = []
    for i in range(tracks_per_catalog):
        isrcs.append(f'US12319{catalog_number[-3:]}{i+1:02d}')
    return isrcs

def make_upc():
    upc = random.randint(10**(12-1), 10**12)
    return upc

def make_versions(catalog_number):
    version_numbers = []
    types = ['dig', 'lp', 'cd', 'cass']
    for type in types:
        version_number = f'{catalog_number}{type}'
        version_numbers.append(version_number)
    return version_numbers

def make_version_items(catalog_number):
    version_items = []
    types = ['dig', 'lp', 'cd', 'cass']
    for type in types:
        entry = {'version_number': f'{catalog_number}{type}',
                'upc': make_upc(),
                }
        version_items.append(entry)
    return version_items

def make_catalog_df(catalogs, artists):
    catalog_items = catalogs.make_catalog_items()
    data = {
            'isrc': [],
            'track_artist': [],
            'track_title': [],
            'catalog_number':[],
            'catalog_artist': [],
            'catalog_name': [],
            }
    for catalog_item in catalog_items:
        # version_items = make_version_items(catalog_item['catalog_number'])
        # for version_item in version_items:
        isrcs = make_track_isrcs(catalog_item['catalog_number'])
        for isrc in isrcs:
            data['isrc'].append(isrc)
            data['track_title'].append(random_phrase())
            if catalog_item['catalog_artist'] == 'Various Artists':
                data['track_artist'].append(artists.random_artist())
            else:
                data['track_artist'].append(catalog_item['catalog_artist'])
            data['catalog_number'].append(catalog_item['catalog_number'])
            data['catalog_artist'].append(catalog_item['catalog_artist'])
            data['catalog_name'].append(catalog_item['catalog_name'])
            # data['upc'].append(version_item['upc'])
            # data['version_number'].append(version_item['version_number'])
    df = pd.DataFrame(data)
    return df

def make_version_df(catalogs):
    catalog_items = catalogs.make_catalog_items()
    data = {
            'upc': [],
            'version_number': [],
            'catalog_number': [],
            }
    for catalog_item in catalog_items:
        version_items = make_version_items(catalog_item['catalog_number'])
        for version_item in version_items:
            data['catalog_number'].append(catalog_item['catalog_number'])
            data['upc'].append(version_item['upc'])
            data['version_number'].append(version_item['version_number'])
    df = pd.DataFrame(data)
    return df

# def make_version_df(catalog_df):
#     df = pd.DataFrame(columns=['upc', 'version_number', 'format', 'version_title', 'catalog_number'])
#     catalog_numbers = find_unique_catalog_numbers(catalog_df)
#     for catalog_number in catalog_numbers:
#         new_df = pd.DataFrame(columns=['upc', 'version_number', 'format', 'version_title', 'catalog_number'])
#         new_df['version_number'] = make_version_numbers(catalog_number)
#         new_df['upc'] = make_upc()
#         new_df['catalog_number'] = catalog_number
#         df = df.append(new_df, ignore_index=True)
#     return df



def main():
    artists = Artists(10)
    catalogs = Catalogs('TR', 5, 2, artists.artist_list)
    catalog_df = make_catalog_df(catalogs, artists)
    version_df = make_version_df(catalogs, artists)
    print(df)
    catalog_df.to_csv('catalog.csv', index=False)
    version_df.to_csv('version.csv', index=False)




if __name__ == '__main__':
    main()
