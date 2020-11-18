import pandas as pd
import os
from faker import Faker

fake = Faker()

def import_csv():
    path = os.getcwd() + '/files/bandcamp.csv'
    df = pd.read_csv(path, encoding='utf-16')
    return df

def find_unique_buyers(df):
    buyer_names = df['buyer name'].unique().tolist()
    return buyer_names

def find_indexes_of_buyer(df, buyer_name):
    indexes = df.index[df['buyer name'] == buyer_name].tolist()
    return indexes

def fake_name():
    first_name = fake.first_name_nonbinary()
    last_name = fake.last_name_nonbinary()
    return first_name + ' ' + last_name

def clean_names(df, indexes):
    for index in indexes:
        df.at[index, 'buyer name'] = fake_name()
        df.at[index, 'buyer email'] = fake.ascii_email()
        df.at[index, 'buyer phone'] = fake.phone_number()
        df.at[index, 'ship to name'] = fake_name()
        df.at[index, 'ship to street'] = fake.street_address()
    return df




def main():
    df = import_csv()
    buyer_names = find_unique_buyers(df)
    for buyer_name in buyer_names:
        indexes = find_indexes_of_buyer(df, buyer_name)
        df = clean_names(df, indexes)
    df.to_csv('out.csv')


if __name__ == '__main__':
    main()
