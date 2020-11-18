from dummy import Catalogs, make_df, make_track_isrcs, Artists


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
    df = make_df(catalogs, artists)
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
    df = make_df(catalogs, artists)
    catalog_numbers = df['catalog_number'].unique().tolist()
    catalog_name_1 = df.loc[df['catalog_number'] == catalog_numbers[0]]['catalog_name'].tolist()
    catalog_name_2 = df.loc[df['catalog_number'] == catalog_numbers[1]]['catalog_name'].tolist()
    assert catalog_name_1[0] != catalog_name_2[0]

    


    


# def test_can_select_catalog_artists():
#     size = 5
#     artists = select_artists(size)

#     def indices_of_various_artists(artists):
#         res = []
#         for index, key in enumerate(artists):
#             if artists[index] == 'Various Artists':
#                 res.append(index)
#         return res
    
#     artists = select_catalog_artists(5, 1)
#     assert len(artists) == 5
#     assert len(indices_of_various_artists(artists)) == 1

#     artists = select_catalog_artists(5, 2)
#     assert len(artists) == 5
#     assert len(indices_of_various_artists(artists)) == 2

#     artists = select_catalog_artists(5, 3)
#     assert len(artists) == 5
#     assert len(indices_of_various_artists(artists)) == 3




# def test_can_find_unique_catalog_numbers():
#     catalog_df = make_catalog_df(5, 0)
#     catalog_numbers = find_unique_catalog_numbers(catalog_df)
#     assert len(catalog_numbers) > 0

# def test_can_make_tracks_df():
#     catalog_df = make_catalog_df(5, 1)
#     df = make_track_df(catalog_df)
#     assert len(df) > 0
#     assert df['isrc'][0] == 'US1231900101'
#     assert df['catalog_number'][0] == 'TR-001'
#     assert df['track_number'][0] == 1
#     assert type(df['track_title'][0]) == str
#     assert df['track_number'][1] == 2
#     assert type(df['track_artist'][0]) == str
#     assert df['isrc'][1] == 'US1231900102'
#     if catalog_df['catalog_artist'][0] != 'Various Artists':
#         assert catalog_df['catalog_artist'][0] == df['track_artist'][0]
#     if catalog_df['catalog_artist'][0] == 'Various Artists':
#         assert str(df['track_artist'][0])
#         assert df['track_artist'][0] != 'Various Artists' 

# def test_can_make_track_artist():
#     artist = make_track_artist()
#     assert type(artist) == str

# def test_can_make_track_title():
#     title = make_track_title()
#     assert type(title) == str

# def test_can_make_version_df():
#     catalog_df = make_catalog_df(5, 0)
#     assert len(catalog_df) > 0
#     df = make_version_df(catalog_df)
#     assert len(df) > 0
#     assert type(df['upc'][0]) == int

# def test_can_make_upc():
#     upc = make_upc()
#     assert len(str(upc)) == 12
    
# def test_can_make_version_numbers():
#     catalog_number = 'TR-001'
#     version_numbers = make_version_numbers(catalog_number)
#     assert len(version_numbers) > 0
