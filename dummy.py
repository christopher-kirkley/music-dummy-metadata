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


def main():
    df = make_catalog_df(5, 3)
    print(df)

    df = pd.DataFrame(columns=['isrc', 'track_artist', 'track_number', 'catalog_number'])


if __name__ == '__main__':
    main()
