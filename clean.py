import pandas as pd
import os
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
    def __init__(self, df):
        self.df = df

    def find_unique_buyers(self):
        buyer_names = self.df['buyer name'].unique().tolist()
        return buyer_names

    def find_indexes_of_buyer(self, buyer_name):
        indexes = self.df.index[self.df['buyer name'] == buyer_name].tolist()
        return indexes

    def clean_names(self):
        buyer_names = self.find_unique_buyers()
        for buyer_name in buyer_names:
            indexes = self.find_indexes_of_buyer(buyer_name)
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






def find_indexes_of_physical_items(df):
    indexes = df.index[df['item type'] == 'package'].tolist()
    return indexes

def load_catalog():
    path = os.getcwd() + '/catalog.csv'
    df = pd.read_csv(path, encoding='utf-8')
    return df

def load_version():
    path = os.getcwd() + '/version.csv'
    df = pd.read_csv(path, encoding='utf-8')
    return df

def change_physical_item(df, indexes):
    for index in indexes:
        df.at[index, 'item name'] = 'd'
    return df




def main():
    df = import_csv()
    df.to_csv('out.csv')


if __name__ == '__main__':
    main()
