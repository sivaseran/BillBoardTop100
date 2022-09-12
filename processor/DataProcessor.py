from reader import CSVReader

from collections import defaultdict, Counter


class DataProcessor:

    def __init__(self, csv_path=None) -> None:
        super().__init__()
        if csv_path:
            self.songs = CSVReader.read(csv_path)
        else:
            self.songs = CSVReader.read("../charts.csv")

    def get_top_ranked_song(self, date):
        for s in self.songs:
            if s.date == date and s.rank == 1:
                return s
        return Exception("song not found")

    def most_top_ranked_songs(self):
        groups = defaultdict(list)
        for s in self.songs:
            if s.rank == 1:
                if s.artist not in groups.keys():
                    groups[s.artist] = 1
                else:
                    groups[s.artist] = groups[s.artist] + 1

        c = Counter(groups)
        return c.most_common(1)[0][0]

    def longest_number_of_weeks_on_board(self, n: int):
        sorted_songs = sorted(self.songs, key=lambda x: x.weeks_on_board, reverse=True)

        return [x.song for x in sorted_songs[0:n]]

    def large_move(self):
        sorted_songs = sorted(self.songs, key=lambda x: x.peak_rank - x.rank, reverse=True)

        return sorted_songs[0].song

    def top_songs(self):
        pass