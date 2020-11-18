from dummy import Catalogs, make_catalog_df, make_track_isrcs, Artists, make_versions, make_upc, make_version_df


def test_pytest_working():
    assert True

def test_can_select_artists():
    artists = Artists(10)
    assert len(artists.artist_list) == 10

def test_can_create_catalog_dict():
    artists = Artists(10)
    catalogs = Catalogs('TR', 5, 1, artists.artist_list)
    catalog_items = catalogs.make_catalog_items()
    assert len(catalog_items) == 5

def test_can_make_catalog_df():
    artists = Artists(10)
    catalogs = Catalogs('TR', 5, 1, artists.artist_list)
    df = make_catalog_df(catalogs, artists)
    artist_list = artists.artist_list
    assert len(df) > 5
    assert df['catalog_number'][0] == 'TR-001'
    assert df['isrc'][0] == 'US1231900101'
    assert type(df['track_artist'][0]) == str
    assert type(df['track_title'][0]) == str
    assert type(df['catalog_artist'][0]) == str
    assert type(df['catalog_name'][0]) == str
    assert df.loc[df['catalog_artist'] == 'Various Artists']['track_artist'][0] != 'Various Artists'
    various_artist_track1 = df.loc[df['catalog_artist'] == 'Various Artists']['track_artist'][0]
    various_artist_track2 = df.loc[df['catalog_artist'] == 'Various Artists']['track_artist'][1]
    assert various_artist_track1 != various_artist_track2
    """check track titles different"""
    track_title_1 = df['track_title'][0]
    track_title_2 = df['track_title'][1]
    assert track_title_1 != track_title_2


def test_can_make_track_isrcs():
    isrcs = make_track_isrcs('TR-001')
    assert len(isrcs) > 0
    assert len(isrcs[0]) == 12
    assert isrcs[0] == 'US1231900101'
    assert isrcs[1] == 'US1231900102'
    artists = Artists(10)
    catalogs = Catalogs('TR', 5, 1, artists.artist_list)
    catalog_items = catalogs.make_catalog_items()
    assert catalog_items[0]['catalog_number'] == 'TR-001'
    isrcs = make_track_isrcs(catalog_items[0]['catalog_number'])
    assert len(isrcs) > 0

def test_can_create_unique_catalog_name():
    artists = Artists(10)
    catalogs = Catalogs('TR', 5, 1, artists.artist_list)
    df = make_catalog_df(catalogs, artists)
    catalog_numbers = df['catalog_number'].unique().tolist()
    catalog_name_1 = df.loc[df['catalog_number'] == catalog_numbers[0]]['catalog_name'].tolist()
    catalog_name_2 = df.loc[df['catalog_number'] == catalog_numbers[1]]['catalog_name'].tolist()
    assert catalog_name_1[0] != catalog_name_2[0]

    
def test_can_make_version_df():
    artists = Artists(10)
    catalogs = Catalogs('TR', 5, 1, artists.artist_list)
    df = make_version_df(catalogs)
    assert len(df) > 0

def test_can_make_upc():
    upc = make_upc()
    assert len(str(upc)) == 12
    
def test_can_make_version_numbers():
    catalog_number = 'TR-001'
    version_numbers = make_versions(catalog_number)
    assert len(version_numbers) > 0
