from db import Db

def __main__():

    database = Db()
    database.check_db()
    database.check_col()

    database.show_sw()

    while True:
        print("Choose an option:")
        print("Type 'i' to insert new software.")
        print("Type 'k' to show keys of a software.")
        print("Type 'ik' to insert a new key into a software.")
        print('Type q to quit program.')

        insert_input = input("Your choice:")

        if insert_input.lower() == "i":
            database.insert_sw()
        elif insert_input.lower() == 'k':
            database.show_keys()
        elif insert_input.lower() == 'ik':
            database.insert_key()
        elif insert_input.lower() == 'q':
            print(quit)
            quit()

if __name__ == "__main__":
    __main__()






