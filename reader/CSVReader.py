import csv
import os

from model.Song import Song


def read(name):
    loaded_data = csv.reader(open(file_path(name)))
    next(loaded_data)
    data = list(loaded_data)

    songs = [Song(data[i][0], int(data[i][1]), data[i][2], data[i][3], int(data[i][4]) if len(data[i][4]) > 0 else 0, int(data[i][5]), int(data[i][6])) for i in range(len(data))]

    return songs


def file_path(relative_path):
    directory = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    new_path = os.path.join(directory, *split_path)
    return new_path
