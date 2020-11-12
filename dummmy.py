import random

import numpy as np
import pandas as pd

from faker import Faker
fake = Faker()

catalog_root = 'TR'
number_of_items = 50

temp = open('./artistnames.txt').read().splitlines()
artist_source = [name.strip() for name in temp]

"""Choose the artists for this instance."""
number_of_artists = 10
artists = [random.choice(artist_source) for artist_name in range(number_of_artists)]



df = pd.DataFrame(columns=['catalog_number', 'catalog_artist', 'catalog_name'])

def random_artist(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    artists = [random.choice(lines).strip() for name in range(number_of_items)]
    return artists

def random_catalog_name(number_of_items):
    lines = open('./artistnames.txt').read().splitlines()
    catalog_names = [random.choice(lines).strip() for name in range(number_of_items)]
    return catalog_names

def generate_catalog_number(number_of_items):
    catalog_numbers = [f'{catalog_root}-0{i}' for i in range(number_of_items)]
    return catalog_numbers

df['catalog_number'] = generate_catalog_number(number_of_items)
df['catalog_artist']= random_artist(number_of_items)
df['catalog_name']= random_catalog_name(number_of_items)

print(df)

df = pd.DataFrame(columns=['isrc', 'track_artist', 'track_number', 'catalog_number'])

