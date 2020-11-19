import os

from clean import import_csv, clean_names, find_unique_buyers, find_indexes_of_buyer, change_info

def test_true():
    assert True

def test_can_make_df():
    df = import_csv()
    assert len(df) > 0

def test_can_clean_names():
    df = import_csv()
    buyer_names = find_unique_buyers(df)
    assert len(buyer_names) > 0

def test_can_find_index_of_buyer():
    df = import_csv()
    buyer_name = 'Lou Bob'
    indexes = find_indexes_of_buyer(df, buyer_name)
    assert len(indexes) == 3
    assert indexes[0] == 1
    assert indexes[1] == 2
    assert df.loc[indexes[0]]['buyer name'] == 'Lou Bob'
    assert df.loc[indexes[1]]['buyer name'] == 'Lou Bob'

def test_can_change_buyer_info():
    df = import_csv()
    buyer_name = 'Lou Bob'
    indexes = find_indexes_of_buyer(df, buyer_name)
    assert df.loc[indexes[0]]['buyer email'] == 'oldemail@gmail.com'
    assert df.loc[indexes[0]]['buyer phone'] == 'oldphone'
    assert df.loc[indexes[0]]['ship to name'] == 'Lou Bob'
    assert df.loc[indexes[0]]['ship to street'] == 'oldaddress'
    df = change_info(df, indexes)
    assert len(df) > 0
    assert type(df.loc[indexes[0]]['buyer name']) == str
    assert df.loc[indexes[0]]['buyer email'] != 'oldemail@gmail.com'
    assert df.loc[indexes[0]]['buyer phone'] != 'oldphone'
    assert df.loc[indexes[0]]['ship to name'] != 'Lou Bob'
    assert df.loc[indexes[0]]['ship to street'] != 'oldaddress'

def test_can_clean_names():
    df = import_csv()
    df = clean_names(df)
    assert df.loc[1]['buyer name'] != 'Lou Bob'
    assert df.loc[1]['buyer email'] != 'oldemail@gmail.com'
    assert df.loc[1]['buyer phone'] != 'oldphone'
    assert df.loc[1]['ship to name'] != 'Lou Bob'
    assert df.loc[1]['ship to street'] != 'oldaddress'


