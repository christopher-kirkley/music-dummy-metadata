from random import randint

import numpy as np
import pandas as pd

from faker import Faker
fake = Faker()

catalog_root = 'TR'
number_of_items = 5

df = pd.DataFrame(columns=['catalog_number', 'catalog_artist', 'catalog_name'])

def random_artist(number_of_items):
    artists = [fake.name() for name in range(number_of_items)]
    return artists

def random_catalog_name(number_of_items):
    catalog = [fake.name() for name in range(number_of_items)]
    return catalog

def generate_catalog_number(number_of_items):
    catalog_numbers = [f'{catalog_root}-0{i}' for i in range(number_of_items)]
    return catalog_numbers

df['catalog_number'] = generate_catalog_number(number_of_items)
df['catalog_artist']= random_artist(number_of_items)
df['catalog_name']= random_catalog_name(number_of_items)

print(df)


