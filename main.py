from db import Db


def main():
    database = Db()

    while True:
        database.show_sw()
        print("\nChoose one of these options please: ")
        print("Type 'i' to insert a new software: ")
        print("Type 'k' if you want to see the keys of a software: ")
        print("Type 'ik' if you want to insert a new key belonging to a software: ")
        print("Type 'q' if you want to quit the program: ")

        insert_input = input("")

        if insert_input.lower() == "i":
            database.insert_sw()
            False
        elif insert_input.lower() == 'k':
            database.show_keys()
            False
        elif insert_input.lower() == 'ik':
            database.insert_key()
            False
        elif insert_input.lower() == 'q':
            print("\n Leaving program... :( ")
            quit()
        else:
            print("Try again.")
            False
           


if __name__ == "__main__":
    main()






