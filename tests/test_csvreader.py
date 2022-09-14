import unittest
from reader import CSVReader
test_csv = "../tests/charts_test.csv"


class TestCsvReader(unittest.TestCase):
    def test_read_csv(self):
        song_list = CSVReader.read(test_csv)
        assert len(song_list) == 9


if __name__ == '__main__':
    unittest.main()
