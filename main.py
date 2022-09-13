
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
        pass
    else:
        print("thanks for choosing our service")
        exit(1)


if __name__ == '__main__':
    main_menu()
