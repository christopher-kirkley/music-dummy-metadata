# music-dummy-metadata
Generate dummy music metadata for testing

This is a small CLI script to create dummy music data for use in testing music based applications.

The output is two CSV files representing a dummy record label's catalog.

Included fields:

### catalog.csv
- ISRC
- Track Number
- Track Title
- Track Artist
- Catalog Number
- Catalog Artist
- Catalog Title

### version.csv
- UPC
- Version Number
- Version Title

## Dependencies

- Pandas
- Pytest (optional)

Source txt for band names comes from Brian Whitman's "Ten Thousand Statistically Grammar-Average Fake Band Names" [https://alumni.media.mit.edu/~bwhitman/10000.html](https://alumni.media.mit.edu/~bwhitman/10000.html)


## Usage

> python dummy.py
