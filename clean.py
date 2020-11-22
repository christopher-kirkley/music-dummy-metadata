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
    def __init__(self, df, catalog_info):
        self.df = df
        self.catalog_info = catalog_info

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
            catalog_item = random.choice(self.catalog_info)
            self.df.at[index, 'catalog number'] = catalog_item['catalog_number']
            self.df.at[index, 'item name'] = catalog_item['catalog_name']
            self.df.at[index, 'artist'] = catalog_item['catalog_artist']
            self.df.at[index, 'sku'] = catalog_item['version_number']
            self.df.at[index, 'upc'] = catalog_item['upc']
            self.df.at[index, 'item url'] = ''
        return self.df


class Catalog():
    def __init__(self, catalog_df, version_df, number_of_items):
        self.catalog_df = catalog_df
        self.version_df = version_df
        self.number_of_items = number_of_items

    def catalog_selection(self):
        catalog_ids = self.catalog_df['catalog_number'].unique().tolist()
        catalog_selection = []
        for i in range(self.number_of_items):
            index = random.randint(0, self.number_of_items)
            catalog_selection.append(catalog_ids[index])
        return catalog_selection

    def find_catalog_info(self):
        catalog_info = []
        for catalog_number in self.catalog_selection():
            version_info = self.find_version_info(catalog_number)
            key = random.randint(0,3)
            entry = {
                    'catalog_number': catalog_number,
                    'catalog_name': version_info['catalog_name'][key],
                    'catalog_artist': version_info['catalog_artist'][key],
                    'version_number': version_info['version_number'][key],
                    'upc': version_info['upc'][key],
                    }
            catalog_info.append(entry)
        return catalog_info

    def find_version_info(self, catalog_number):
        version_info = []
        new_catalog_df = self.catalog_df.copy()
        new_catalog_df.drop(
                [
                'track_artist',
                'track_title',
                'isrc'],
                axis=1,
                inplace=True
                )
        joined_df = new_catalog_df.merge(self.version_df, on='catalog_number')
        version_df_selection = joined_df.loc[joined_df['catalog_number'] == catalog_number]
        version_df_selection.drop_duplicates(inplace=True)
        return version_df_selection.to_dict('list')


def load_catalog():
    path = os.getcwd() + '/catalog.csv'
    df = pd.read_csv(path, encoding='utf-8')
    return df

def load_version():
    path = os.getcwd() + '/version.csv'
    df = pd.read_csv(path, encoding='utf-8')
    return df


def main():
    df = import_csv()
    df.to_csv('out.csv')


if __name__ == '__main__':
    main()
