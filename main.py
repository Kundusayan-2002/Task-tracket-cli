from src.cli import populate_menu
def main():
    menu = populate_menu()
    while True:
        print(menu)

        user_input = input(">> ")
if __name__ == "__main__":
    main()