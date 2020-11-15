import random

import numpy as np
import pandas as pd

from faker import Faker
fake = Faker()

catalog_root = 'TR'
number_of_items = 50

def make_artist_list():
    temp = open('./artistnames.txt').read().splitlines()
    artist_source = [name.strip() for name in temp]
    return artist_source


def select_artists(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    artists = [random.choice(lines).strip() for name in range(number_of_items)]
    return artists

def select_catalog_artists(size, size_va):
    artists = select_artists(size)
    for i in range(size_va):
        artists[i] = 'Various Artists'
    return artists

def select_catalog(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    catalog_names = [random.choice(lines).strip() for name in range(number_of_items)]
    return catalog_names

def make_catalog_numbers(catalog_root, number_of_items):
    catalog_numbers = [f'{catalog_root}-00{i}' for i in range(1, number_of_items+1)]
    return catalog_numbers

def make_catalog_df(size, size_va):
    df = pd.DataFrame(columns=['catalog_number', 'catalog_artist', 'catalog_name'])
    df['catalog_number'] = make_catalog_numbers(catalog_root, size)
    df['catalog_artist']= select_catalog_artists(size, size_va)
    df['catalog_name']= select_catalog(size)
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
            new_df['track_artist'] = 'Various Artists'
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
    types = ['digi', 'lp', 'cd', 'cass']
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
        print(new_df)
        df = df.append(new_df, ignore_index=True)
    print(df)
    return df



def main():
    catalog_df = make_catalog_df(5, 3)
    catalog_df.to_csv('catalog.csv')
    track_df = make_track_df(catalog_df)
    track_df.to_csv('track.csv')



if __name__ == '__main__':
    main()
