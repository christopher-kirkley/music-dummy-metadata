import os

import pytest

from clean import Bandcamp_df, make_df

def make_catalog_json():
    catalog_json = [
            {
                'catalog_number': 'TR-001',
                'catalog_name': 'Cheeseburger',
                'catalog_artist': 'Stevie B.',
                'versions': [
                    {
                        'version_number': 'TR-001lp',
                        'version_name': 'Vinyl',
                        'upc': '1234567',
                        },
                    ],
                'tracks': [
                    {
                        'track_number': 1,
                        'track_artist': 'Stevie B.',
                        'track_name': 'Babaloo',
                        'isrc': 'QA123',
                        },
                    ]
                    }
            ]
    return catalog_json

@pytest.fixture
def bandcamp_df():
    catalog_json = make_catalog_json()
    df = make_df()
    bandcamp_df = Bandcamp_df(df, catalog_json)
    yield bandcamp_df

def test_can_create_df():
    df = make_df()
    assert len(df) > 0

def test_can_initialize_bandcamp_df():
    catalog_json = make_catalog_json()
    df = make_df()
    bandcamp_df = Bandcamp_df(df, catalog_json)
    assert len(df) == len(bandcamp_df.df)
    assert len(bandcamp_df.catalog_json) > 0

def test_can_clean_names(bandcamp_df):
    buyer_names = bandcamp_df.find_unique_buyers()
    assert len(buyer_names) > 0

def test_can_find_index_of_buyer(bandcamp_df):
    buyer_name = 'Lou Bob'
    indexes = bandcamp_df.buyer_indexes(buyer_name)
    assert len(indexes) == 3
    assert indexes[0] == 1
    assert indexes[1] == 2
    assert bandcamp_df.df.loc[indexes[0]]['buyer name'] == 'Lou Bob'
    assert bandcamp_df.df.loc[indexes[1]]['buyer name'] == 'Lou Bob'

def test_can_find_indexes_of_buyer(bandcamp_df):
    buyer_name = 'Lou Bob'
    indexes = bandcamp_df.buyer_indexes(buyer_name)
    assert bandcamp_df.df.loc[indexes[0]]['buyer email'] == 'oldemail@gmail.com'
    assert bandcamp_df.df.loc[indexes[0]]['buyer phone'] == 'oldphone'
    assert bandcamp_df.df.loc[indexes[0]]['ship to name'] == 'Lou Bob'
    assert bandcamp_df.df.loc[indexes[0]]['ship to street'] == 'oldaddress'
    df = bandcamp_df.change_info(indexes)
    assert len(df) > 0
    assert type(df.loc[indexes[0]]['buyer name']) == str
    assert df.loc[indexes[0]]['buyer email'] != 'oldemail@gmail.com'
    assert df.loc[indexes[0]]['buyer phone'] != 'oldphone'
    assert df.loc[indexes[0]]['ship to name'] != 'Lou Bob'
    assert df.loc[indexes[0]]['ship to street'] != 'oldaddress'

def test_can_clean_two(bandcamp_df):
    df = bandcamp_df.clean_names()
    assert df.loc[1]['buyer name'] != 'Lou Bob'
    assert df.loc[1]['buyer email'] != 'oldemail@gmail.com'
    assert df.loc[1]['buyer phone'] != 'oldphone'
    assert df.loc[1]['ship to name'] != 'Lou Bob'
    assert df.loc[1]['ship to street'] != 'oldaddress'

def test_can_find_indexes_of_physical_items(bandcamp_df):
    indexes = bandcamp_df.physical_indexes()
    assert len(indexes) > 0
    assert indexes[0] == 1
    assert indexes[1] == 5
    assert bandcamp_df.df.loc[indexes[0]]['item name'] == 'Eghass Malan'
    assert bandcamp_df.df.loc[indexes[1]]['item name'] == 'Anou Malane'

def test_can_change_physical_item(bandcamp_df):
    indexes = bandcamp_df.physical_indexes()
    assert len(indexes) > 0
    bandcamp_df.change_physical_item(indexes)
    assert bandcamp_df.df.loc[1]['catalog number'] == 'TR-001'
    assert bandcamp_df.df.loc[1]['item name'] == 'Bobo'
    assert bandcamp_df.df.loc[1]['artist'] == 'Tomato Jones'
    assert bandcamp_df.df.loc[1]['sku'] == 'TR-001lp'
    assert bandcamp_df.df.loc[1]['upc'] == '1234'
    assert bandcamp_df.df.loc[1]['item url'] == ''

def test_can_change_physical_item_functional(bandcamp_df):
    indexes = bandcamp_df.physical_indexes()
    df = bandcamp_df.change_physical_item(indexes)
    assert df.loc[1]['catalog number'].startswith('TR-00')
    assert type(df.loc[1]['item name']) == str
    assert type(df.loc[1]['artist']) == str
    assert df.loc[1]['sku'].startswith('TR-00')
    assert type(df.loc[1]['upc']) == int
    assert df.loc[1]['item url'] == ''


