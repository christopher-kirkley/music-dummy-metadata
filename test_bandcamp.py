import os

from clean import find_indexes_of_physical_items, load_catalog, load_version,change_physical_item, make_df

from clean import Bandcamp_df

def test_true():
    assert True

def test_can_create_df():
    df = make_df()
    assert len(df) > 0

def test_can_initialize_bandcamp_df():
    df = make_df()
    bandcamp = Bandcamp_df(df)
    assert len(df) == len(bandcamp.df)

def test_can_clean_names():
    buyer_names = bandcamp.find_unique_buyers(df)
    assert len(buyer_names) > 0

def test_can_find_index_of_buyer():
    df = make_df()
    bandcamp = Bandcamp_df(df)
    buyer_name = 'Lou Bob'
    indexes = bandcamp.find_indexes_of_buyer(buyer_name)
    assert len(indexes) == 3
    assert indexes[0] == 1
    assert indexes[1] == 2
    assert df.loc[indexes[0]]['buyer name'] == 'Lou Bob'
    assert df.loc[indexes[1]]['buyer name'] == 'Lou Bob'

def test_can_change_buyer_info():
    df = make_df()
    bandcamp = Bandcamp_df(df)
    buyer_name = 'Lou Bob'
    indexes = bandcamp.find_indexes_of_buyer(buyer_name)
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
    df = make_df()
    bandcamp = Bandcamp_df(df)
    df = bandcamp.clean_names()
    assert df.loc[1]['buyer name'] != 'Lou Bob'
    assert df.loc[1]['buyer email'] != 'oldemail@gmail.com'
    assert df.loc[1]['buyer phone'] != 'oldphone'
    assert df.loc[1]['ship to name'] != 'Lou Bob'
    assert df.loc[1]['ship to street'] != 'oldaddress'

def test_can_find_indexes_of_physical_items():
    df = make_df()
    bandcamp = Bandcamp_df(df)
    indexes = find_indexes_of_physical_items(df)
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
    df = make_df()
    catalog_df = load_catalog()
    version_df = load_version()
    indexes = find_indexes_of_physical_items(df)
    df = change_physical_item(df, indexes)
    assert df.loc[1]['item name'] == 'Eghass Malan'

def test_can_get_catalog_item():
    catalog_df = load_catalog()

