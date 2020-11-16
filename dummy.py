import random

import numpy as np
import pandas as pd

from faker import Faker
fake = Faker()

catalog_root = 'TR'
number_of_items = 50

class Artists():
    def __init__(self, number_of_artists):
        self.number_of_artists = number_of_artists

    def make_artist_list(self):
        temp = open('./artistnames.txt').read().splitlines()
        artist_source = [name.strip() for name in temp]
        return artist_source

def select_artists(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    artists = [random.choice(lines).strip() for name in range(number_of_items)]
    return artists


class Catalogs():
    def __init__(self, catalog_root, number_of_items, size_va):
        self.catalog_root = catalog_root
        self.number_of_items = number_of_items

    def select_catalog_artists(self):
        artists = select_artists(self.number_of_items)
        for i in range(self.size_va):
            artists[i] = 'Various Artists'
        return artists

    def select_catalog(self):
        lines = open('./artistnames.txt').read().splitlines()
        catalog_names = [random.choice(lines).strip() for name in range(self.number_of_items)]
        return catalog_names

    def make_catalog_numbers(self):
        catalog_numbers = [f'{self.catalog_root}-00{i}' for i in range(1, self.number_of_items+1)]
        return catalog_numbers

    def make_catalog_df(self):
        df = pd.DataFrame(columns=['catalog_number', 'catalog_artist', 'catalog_name'])
        df['catalog_number'] = self.make_catalog_numbers()
        df['catalog_artist']= self.select_catalog_artists()
        df['catalog_name']= self.select_catalog()
        return df



def make_track_artist():
    artist = select_artists(1)[0]
    return artist

def make_track_title():
    title = select_catalog(1)[0]
    return title

def make_track_isrcs(catalog_number):
    tracks_per_catalog = random.randint(2, 10)
    isrcs = []
    for i in range(tracks_per_catalog):
        isrcs.append(f'US12319{catalog_number[-3:]}{i+1:02d}')
    return isrcs

def find_unique_catalog_numbers(catalog_df):
    catalog_numbers = catalog_df['catalog_number'].unique().tolist()
    return catalog_numbers

class tracks:
    def __init__(self):
        pass

    def make_df(self):
        pass


def make_track_df(catalog_df):
    df = pd.DataFrame(columns=['isrc', 'track_number', 'track_artist', 'track_title', 'catalog_number'])
    catalog_numbers = find_unique_catalog_numbers(catalog_df)
    for catalog_number in catalog_numbers:
        new_df = pd.DataFrame(columns=['isrc', 'track_artist', 'track_number', 'track_title', 'catalog_number'])
        new_df['isrc'] = make_track_isrcs(catalog_number)
        new_df['catalog_number'] = catalog_number
        new_df['track_artist'] = make_track_artist()
        catalog_artist = catalog_df.loc[catalog_df['catalog_number'] == catalog_number]['catalog_artist'].tolist()[0]
        if catalog_artist == 'Various Artists':
            new_df['track_artist'] = make_track_artist()
        else:
            new_df['track_artist'] = catalog_artist
        for index, row in enumerate(new_df.iterrows()):
            new_df['track_number'][index] = index + 1
            new_df['track_title'][index] = make_track_title()
        df = df.append(new_df, ignore_index=True)

    return df

def make_upc():
    upc = random.randint(10**(12-1), 10**12)
    return upc

def make_version_numbers(catalog_number):
    version_numbers = []
    types = ['dig', 'lp', 'cd', 'cass']
    for type in types:
        version_number = f'{catalog_number}{type}'
        version_numbers.append(version_number)
    return version_numbers


def make_version_df(catalog_df):
    df = pd.DataFrame(columns=['upc', 'version_number', 'format', 'version_title', 'catalog_number'])
    catalog_numbers = find_unique_catalog_numbers(catalog_df)
    for catalog_number in catalog_numbers:
        new_df = pd.DataFrame(columns=['upc', 'version_number', 'format', 'version_title', 'catalog_number'])
        new_df['version_number'] = make_version_numbers(catalog_number)
        new_df['upc'] = make_upc()
        new_df['catalog_number'] = catalog_number
        df = df.append(new_df, ignore_index=True)
    return df



def main():
    catalog_df = make_catalog_df(5, 3)
    catalog_df.to_csv('catalog.csv')
    track_df = make_track_df(catalog_df)
    track_df.to_csv('track.csv')



if __name__ == '__main__':
    main()
