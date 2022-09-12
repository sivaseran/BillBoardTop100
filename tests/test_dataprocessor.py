import pytest
# test_data_processor.py
from processor import DataProcessor
test_csv = "../tests/charts_test.csv"


def test_get_top_ranked_song():
    top_song = DataProcessor(test_csv).get_top_ranked_song('2021-11-06')
    assert top_song.artist == "Adele" and top_song.song == "Easy On Me"


def test_most_top_ranked_songs():
    artist = DataProcessor(test_csv).most_top_ranked_songs()
    assert artist == "Adele"