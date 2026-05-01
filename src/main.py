from cli.menu import show_menu
from db.database import create_tables


def main():
    create_tables()
    show_menu()
    


if __name__ == "__main__":
    main()
        