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


df = pd.DataFrame(columns=['catalog_number', 'catalog_artist', 'catalog_name'])

def select_artists(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    artists = [random.choice(lines).strip() for name in range(number_of_items)]
    return artists

def select_catalog(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    catalog_names = [random.choice(lines).strip() for name in range(number_of_items)]
    return catalog_names

def make_catalog_numbers(catalog_root, number_of_items):
    catalog_numbers = [f'{catalog_root}-00{i}' for i in range(1, number_of_items+1)]
    return catalog_numbers

def main():
    df['catalog_number'] = generate_catalog_number(number_of_items)
    df['catalog_artist']= random_artist(number_of_items)
    df['catalog_name']= random_catalog_name(number_of_items)

    print(df)

    df = pd.DataFrame(columns=['isrc', 'track_artist', 'track_number', 'catalog_number'])


if __name__ == '__main__':
    main()
