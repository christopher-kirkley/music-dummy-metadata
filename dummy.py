import random

import numpy as np
import pandas as pd

from collections import defaultdict

from faker import Faker
fake = Faker()

catalog_root = 'TR'
number_of_items = 50

class Catalogs():
    def __init__(self, catalog_root, number_of_catalogs, size_va):
        self.catalog_root = catalog_root
        self.number_of_catalogs = number_of_catalogs
        self.size_va = size_va

    def select_catalog_artists(self):
        artists = make_artist_list(self.number_of_catalogs)
        for i in range(self.size_va):
            artists[i] = 'Various Artists'
        return artists

    def select_catalog(self):
        lines = open('./artistnames.txt').read().splitlines()
        catalog_names = [random.choice(lines).strip() for name in range(self.number_of_catalogs)]
        return catalog_names

    def make_catalog_numbers(self):
        catalog_numbers = [f'{self.catalog_root}-00{i}' for i in range(1, self.number_of_catalogs+1)]
        return catalog_numbers

def make_artist_list(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    artist_list = [random.choice(lines).strip() for name in range(number_of_items)]
    return artist_list

def random_phrase(artist_list):
    index = random.randint(1, 9)
    phrase = artist_list[index]
    return phrase


# def find_unique_catalog_numbers(catalog_df):
#     catalog_numbers = catalog_df['catalog_number'].unique().tolist()
#     return catalog_numbers

def make_track_isrcs(catalog_number):
    tracks_per_catalog = random.randint(2, 10)
    isrcs = []
    for i in range(tracks_per_catalog):
        isrcs.append(f'US12319{catalog_number[-3:]}{i+1:02d}')
    return isrcs

def make_df(catalogs):
    artist_list= make_artist_list(10)
    catalog_numbers = catalogs.make_catalog_numbers()
    data = {
            'isrc': [],
            'track_artist': [],
            'track_title': [],
            'catalog_number':[],
            'catalog_artist': [],
            'catalog_name': []
            }
    for catalog_number in catalog_numbers:
        isrcs = make_track_isrcs(catalog_number)
        for isrc in isrcs:
            data['isrc'].append(isrc)
            data['track_artist'].append(random_phrase(artist_list))
            data['track_title'].append('cheese')
            data['catalog_number'].append(catalog_number)
            data['catalog_artist'].append('3')
            data['catalog_name'].append('name')
    df = pd.DataFrame(data)
    return df
        


#     catalog_numbers = find_unique_catalog_numbers(catalog_df)
#     for catalog_number in catalog_numbers:

        # new_df = pd.DataFrame(columns=['isrc', 'track_artist', 'track_number', 'track_title', 'catalog_number'])
        # new_df['isrc'] = make_track_isrcs(catalog_number)
        # new_df['catalog_number'] = catalog_number
        # new_df['track_artist'] = make_track_artist()
        # catalog_artist = catalog_df.loc[catalog_df['catalog_number'] == catalog_number]['catalog_artist'].tolist()[0]
        # if catalog_artist == 'Various Artists':
        #     new_df['track_artist'] = make_track_artist()
        # else:
        #     new_df['track_artist'] = catalog_artist
        # for index, row in enumerate(new_df.iterrows()):
        #     new_df['track_number'][index] = index + 1
        #     new_df['track_title'][index] = make_track_title()
        # df = df.append(new_df, ignore_index=True)
    





class Tracks():
    def __init__(self):
        pass


# def make_track_artist():
#     artist = select_artists(1)[0]
#     return artist

# def make_track_title():
#     title = select_catalog(1)[0]
#     return title





# def make_track_df(catalog_df):
#     df = pd.DataFrame(columns=['isrc', 'track_number', 'track_artist', 'track_title', 'catalog_number'])

#     return df

# def make_upc():
#     upc = random.randint(10**(12-1), 10**12)
#     return upc

# def make_version_numbers(catalog_number):
#     version_numbers = []
#     types = ['dig', 'lp', 'cd', 'cass']
#     for type in types:
#         version_number = f'{catalog_number}{type}'
#         version_numbers.append(version_number)
#     return version_numbers


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
    catalogs = Catalogs('TR', 5, 2)
    df = make_df(catalogs)
    print(df)




if __name__ == '__main__':
    main()
