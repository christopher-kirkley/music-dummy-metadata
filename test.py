from dummy import make_artist_list, select_artists, select_catalog, make_catalog_numbers


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
