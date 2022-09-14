import unittest
# test_data_processor.py
from processor import DataProcessor
test_csv = "../tests/charts_test.csv"


class TestDataProcessor(unittest.TestCase):
    def test_get_top_ranked_song(self):
        top_song = DataProcessor(test_csv).get_top_ranked_song('2021-11-06')
        assert top_song.artist == "Adele" and top_song.song == "Easy On Me"

    def test_most_top_ranked_songs(self):
        artist = DataProcessor(test_csv).most_top_ranked_songs_artist()
        assert artist == "Adele"

    def test_longest_number_of_weeks_on_board(self):
        song = DataProcessor(test_csv).longest_number_of_weeks_on_board(2)
        assert song[0] == "Fancy Like"
        assert song[1] == "Stay"

    def test_large_move(self):
        song = DataProcessor(test_csv).large_move()
        assert song == "Industry Baby"


if __name__ == '__main__':
    unittest.main()