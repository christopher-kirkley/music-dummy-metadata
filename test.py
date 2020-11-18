import pytest

from dummy import Artists, Catalogs, Isrcs


def test_pytest_working():
    assert True

def test_get_selection_of_working_artists():
    artists = Artists(5)
    artist_selection = artists.select_artists()
    assert len(artist_selection) == 5

def test_get_selection_of_catalog():
    artists = Artists(5)
    catalogs = Catalogs('TR', 5, 1, artists)
    catalog_selection = catalogs.select_catalog()
    assert len(catalog_selection) == 5

def test_create_catalog_numbers():
    artists = Artists(5)
    catalogs = Catalogs('TR', 5, 1, artists)
    catalog_numbers = catalogs.make_catalog_numbers()
    assert len(catalog_numbers) > 0
    assert catalog_numbers[0] == 'TR-001'

def test_can_make_catalog_df():
    artists = Artists(5)
    catalogs = Catalogs('TR', 5, 1, artists)
    df = catalogs.make_catalog_df()
    assert len(df) == 5
    assert df['catalog_number'][0] == 'TR-001'
    assert type(df['catalog_artist'][0]) == str
    assert type(df['catalog_name'][0]) == str

def test_can_select_catalog_artists():
    artists = Artists(5)
    catalogs = Catalogs('TR', 5, 1, artists)
    catalog_artists = catalogs.select_catalog_artists()

    def indices_of_various_artists(catalog_artists):
        res = []
        for index, key in enumerate(catalog_artists):
            if catalog_artists[index] == 'Various Artists':
                res.append(index)
        return res
    
    catalog_artists = catalogs.select_catalog_artists()
    assert len(catalog_artists) == 5
    assert len(indices_of_various_artists(catalog_artists)) == 1

def test_can_make_track_isrcs():
    artists = Artists(5)
    catalogs = Catalogs('TR', 5, 1, artists)
    catalog_df = catalogs.make_catalog_df()
    isrcs = Isrcs(catalogs, artists, catalog_df)
    isrc_selection = isrcs.make_track_isrcs('TR-001')
    assert len(isrc_selection) > 0
    assert len(isrc_selection[0]) == 12
    assert isrc_selection[0] == 'US1231900101'
    assert isrc_selection[1] == 'US1231900102'


def test_can_find_unique_catalog_numbers():
    artists = Artists(5)
    catalogs = Catalogs('TR', 5, 1, artists)
    catalog_df = catalogs.make_catalog_df()
    isrcs = Isrcs(catalogs, artists, catalog_df)
    catalog_numbers = isrcs.find_unique_catalog_numbers()
    assert len(catalog_numbers) > 0

def test_can_make_tracks_df():
    catalog_df = make_catalog_df(5, 1)
    df = make_track_df(catalog_df)
    assert len(df) > 0
    assert df['isrc'][0] == 'US1231900101'
    assert df['catalog_number'][0] == 'TR-001'
    assert df['track_number'][0] == 1
    assert type(df['track_title'][0]) == str
    assert df['track_number'][1] == 2
    assert type(df['track_artist'][0]) == str
    assert df['isrc'][1] == 'US1231900102'
    if catalog_df['catalog_artist'][0] != 'Various Artists':
        assert catalog_df['catalog_artist'][0] == df['track_artist'][0]
    if catalog_df['catalog_artist'][0] == 'Various Artists':
        assert str(df['track_artist'][0])
        assert df['track_artist'][0] != 'Various Artists' 

def test_can_make_track_artist():
    artist = make_track_artist()
    assert type(artist) == str

def test_can_make_track_title():
    title = make_track_title()
    assert type(title) == str

def test_can_make_version_df():
    catalog_df = make_catalog_df(5, 0)
    assert len(catalog_df) > 0
    df = make_version_df(catalog_df)
    assert len(df) > 0
    assert type(df['upc'][0]) == int

def test_can_make_upc():
    upc = make_upc()
    assert len(str(upc)) == 12
    
def test_can_make_version_numbers():
    catalog_number = 'TR-001'
    version_numbers = make_version_numbers(catalog_number)
    assert len(version_numbers) > 0
