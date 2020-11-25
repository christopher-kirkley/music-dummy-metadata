import os

from clean import load_catalog, load_version, make_df

from clean import Bandcamp_df, Catalog

def make_test_json():
    catalog_json = {
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

def test_can_create_df():
    df = make_df()
    assert len(df) > 0

def test_can_initialize_bandcamp_df():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_info = catalog.find_catalog_info()
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_info)
    assert len(df) == len(bandcamp.df)

def test_can_clean_names():
    buyer_names = bandcamp.find_unique_buyers(df)
    assert len(buyer_names) > 0

def test_can_find_index_of_buyer():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_info = catalog.find_catalog_info()
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_info)
    buyer_name = 'Lou Bob'
    indexes = bandcamp.buyer_indexes(buyer_name)
    assert len(indexes) == 3
    assert indexes[0] == 1
    assert indexes[1] == 2
    assert df.loc[indexes[0]]['buyer name'] == 'Lou Bob'
    assert df.loc[indexes[1]]['buyer name'] == 'Lou Bob'

def test_can_find_indexes_of_buyer():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_info = catalog.find_catalog_info()
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_info)
    buyer_name = 'Lou Bob'
    indexes = bandcamp.buyer_indexes(buyer_name)
    assert df.loc[indexes[0]]['buyer email'] == 'oldemail@gmail.com'
    assert df.loc[indexes[0]]['buyer phone'] == 'oldphone'
    assert df.loc[indexes[0]]['ship to name'] == 'Lou Bob'
    assert df.loc[indexes[0]]['ship to street'] == 'oldaddress'
    df = bandcamp.change_info(indexes)
    assert len(df) > 0
    assert type(df.loc[indexes[0]]['buyer name']) == str
    assert df.loc[indexes[0]]['buyer email'] != 'oldemail@gmail.com'
    assert df.loc[indexes[0]]['buyer phone'] != 'oldphone'
    assert df.loc[indexes[0]]['ship to name'] != 'Lou Bob'
    assert df.loc[indexes[0]]['ship to street'] != 'oldaddress'

def test_can_clean_names():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_info = catalog.find_catalog_info()
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_info)
    df = bandcamp.clean_names()
    assert df.loc[1]['buyer name'] != 'Lou Bob'
    assert df.loc[1]['buyer email'] != 'oldemail@gmail.com'
    assert df.loc[1]['buyer phone'] != 'oldphone'
    assert df.loc[1]['ship to name'] != 'Lou Bob'
    assert df.loc[1]['ship to street'] != 'oldaddress'

def test_can_find_indexes_of_physical_items():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_info = catalog.find_catalog_info()
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_info)
    indexes = bandcamp.physical_indexes()
    assert len(indexes) > 0
    assert indexes[0] == 1
    assert indexes[1] == 5
    assert df.loc[indexes[0]]['item name'] == 'Eghass Malan'
    assert df.loc[indexes[1]]['item name'] == 'Anou Malane'

def test_can_load_catalog():
    catalog_df = load_catalog()
    assert len(catalog_df) > 0

def test_can_load_version():
    version_df = load_version()
    assert len(version_df) > 0

def test_can_change_physical_item():
    catalog_info = [
            {
                'catalog_number': 'TR-001',
                'catalog_name': 'Bobo',
                'catalog_artist': 'Tomato Jones',
                'version': [
                    {
                        'version_number': 'TR-001lp',
                        'upc': '1234',
                        },
                    {
                        'version_number': 'TR-001lp',
                        'upc': '1234',
                        },
                    {
                        'version_number': 'TR-001lp',
                        'upc': '1234',
                        },
                    {
                        'version_number': 'TR-001lp',
                        'upc': '1234',
                        },
                    ]
                }
                    
                ]
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_info)
    indexes = bandcamp.physical_indexes()
    df = bandcamp.change_physical_item(indexes)
    assert df.loc[1]['catalog number'] == 'TR-001'
    assert df.loc[1]['item name'] == 'Bobo'
    assert df.loc[1]['artist'] == 'Tomato Jones'
    assert df.loc[1]['sku'] == 'TR-001lp'
    assert df.loc[1]['upc'] == '1234'
    assert df.loc[1]['item url'] == ''

def test_can_get_catalog_selection():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    assert len(catalog.catalog_selection()) == 3
    
def test_can_find_catalog_info():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_info = catalog.find_catalog_info()
    assert len(catalog_info) == 3

def test_can_change_physical_item_functional():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 1)
    catalog_info = catalog.find_catalog_info()
    df = make_df()
    bandcamp = Bandcamp_df(df, catalog_info)
    indexes = bandcamp.physical_indexes()
    df = bandcamp.change_physical_item(indexes)
    assert df.loc[1]['catalog number'].startswith('TR-00')
    assert type(df.loc[1]['item name']) == str
    assert type(df.loc[1]['artist']) == str
    assert df.loc[1]['sku'].startswith('TR-00')
    assert type(df.loc[1]['upc']) == int
    assert df.loc[1]['item url'] == ''

def test_can_make_catalog_entry_df():
    catalog_df = load_catalog()
    version_df = load_version()
    catalog = Catalog(catalog_df, version_df, 3)
    catalog_number = 'TR-001'
    version_info = catalog.find_version_info(catalog_number)
    assert len(version_info) > 0
    assert version_info == ''

