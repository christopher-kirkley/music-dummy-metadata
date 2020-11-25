import os
import random

import pandas as pd
from faker import Faker

fake = Faker()

def make_df():
    path = os.getcwd() + '/files/bandcamp.csv'
    df = pd.read_csv(path, encoding='utf-16')
    return df

def fake_name():
    first_name = fake.first_name_nonbinary()
    last_name = fake.last_name_nonbinary()
    return first_name + ' ' + last_name

class Bandcamp_df():
    def __init__(self, df, catalog_json):
        self.df = df
        self.catalog_json = catalog_json

    def find_unique_buyers(self):
        buyer_names = self.df['buyer name'].unique().tolist()
        return buyer_names

    def buyer_indexes(self, buyer_name):
        indexes = self.df.index[self.df['buyer name'] == buyer_name].tolist()
        return indexes

    def clean_names(self):
        buyer_names = self.find_unique_buyers()
        for buyer_name in buyer_names:
            indexes = self.buyer_indexes(buyer_name)
            self.df = self.change_info(indexes)
        return self.df

    def change_info(self, indexes):
        new_name = fake_name()
        for index in indexes:
            self.df.at[index, 'buyer name'] = new_name
            self.df.at[index, 'buyer email'] = fake.ascii_email()
            self.df.at[index, 'buyer phone'] = fake.phone_number()
            self.df.at[index, 'ship to name'] = fake_name()
            self.df.at[index, 'ship to street'] = fake.street_address()
        return self.df

    def physical_indexes(self):
        indexes = self.df.index[self.df['item type'] == 'package'].tolist()
        return indexes

    def change_physical_item(self, indexes):
        for index in indexes:
            key = random.randint(0, 3)
            catalog_item = random.choice(self.catalog_json)
            self.df.at[index, 'catalog number'] = catalog_item['catalog_number']
            self.df.at[index, 'item name'] = catalog_item['catalog_name']
            self.df.at[index, 'artist'] = catalog_item['catalog_artist']
            self.df.at[index, 'sku'] = catalog_item['versions'][key]['versions_number']
            self.df.at[index, 'upc'] = catalog_item['versions'][key]['upc']
            self.df.at[index, 'item url'] = ''
        return self.df



def main():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_json = catalog.find_catalog_json()
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_json)
    indexes = bandcamp.physical_indexes()
    df = bandcamp.change_physical_item(indexes)

    df.to_csv('out.csv')


if __name__ == '__main__':
    main()
