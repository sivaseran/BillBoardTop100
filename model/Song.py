class Song:
    def __init__(self, date, rank: int, song, artist, last_week: int, peak_rank: int, weeks_on_board: int):
        super().__init__()
        self.date = date
        self.rank = rank
        self.song = song
        self.artist = artist
        self.last_week = last_week
        self.peak_rank = peak_rank
        self.weeks_on_board = weeks_on_board
