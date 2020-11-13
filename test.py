from dummy import make_artist_list, select_artists, select_catalog, make_catalog_numbers, make_catalog_df, select_catalog_artists


def test_pytest_working():
    assert True

def test_can_make_artist_list():
    artist_source = make_artist_list()
    assert len(artist_source) > 0

def test_get_selection_of_working_artists():
    size = 5
    artist_selection = select_artists(5)
    assert len(artist_selection) == 5

def test_get_selection_of_catalog():
    size = 5
    catalog_selection = select_catalog(5)
    assert len(catalog_selection) == 5

def test_create_catalog_numbers():
    root = 'TR'
    size = 5
    catalog_numbers = make_catalog_numbers(root, size)
    assert len(catalog_numbers) > 0
    assert catalog_numbers[0] == 'TR-001'

def test_can_make_catalog_df():
    size = 5
    size_va = 0
    df = make_catalog_df(size, size_va)
    assert len(df) == 5
    assert df['catalog_number'][0] == 'TR-001'
    assert type(df['catalog_artist'][0]) == str
    assert type(df['catalog_name'][0]) == str

def test_can_select_catalog_artists():
    size = 5
    artists = select_artists(size)

    def va_list(artists):
        res = []
        for index, key in enumerate(artists):
            if artists[index] == 'Various Artists':
                res.append(index)
        return res
    
    artists = select_catalog_artists(5, 1)
    assert len(artists) == 5
    assert len(va_list(artists)) == 1
