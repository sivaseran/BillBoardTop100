from processor import DataProcessor

data_processor = DataProcessor()


def main_menu():
    print("Welcome to BillBoard 100, Please select the option from below menu")
    print("""
    1. top ranked song of the day
    2. artist who has most top ranked songs
    3. 10 songs which had longest weeks on the board
    4. song which has moved most ranks
    5. visualize top songs
    6. exit
    """)
    inp = input("please select the option: ")
    print("showing option " + inp)
    i = int(inp)
    if i == 1:
        date = input("please select a day in the format (yyyy-MM-dd): ")
        song = data_processor.get_top_ranked_song(date)
        print("Top song of the date " + date + " is " + song.song)
        main_menu()
    elif i == 2:
        artist = data_processor.most_top_ranked_songs_artist()
        print("Most top ranked song artist : " + artist)
        main_menu()
    elif i == 3:
        songs = data_processor.longest_number_of_weeks_on_board(10)
        print("10 songs which had longest weeks on the board")
        for i in range(10):
            print(str(i + 1) + ". " + songs[i])
        print("\n")
        main_menu()
    else:
        print("thanks for choosing our service")
        exit(1)


if __name__ == '__main__':
    main_menu()
