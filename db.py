# TO DO: Imports
import os
import pymongo

class Db():

    def __init__(self):
        self.connectionstring = os.getenv("CS_MONGODB")
        self.client = pymongo.MongoClient(self.connectionstring)
        self.db_list = self.client.list_database_names()
        self.col_list = self.client.list_collection_names()
        self.db = "Softwares"
        self.col = "Keys"

    def create_db(self):
        self.client[self.db]
        print("Database created!")

    def create_col(self):
        self.client[self.db][self.col]
        print("Collection created!")

    def check_db(self):
        if self.db not in self.db_list:
            db_input = input("Type 'y' if you want to create a database and 'n' if not.")
            if db_input.lower() == "y":
                self.create_db()
            else:
                print(exit)
                exit()

    def check_col(self):
        if self.col not in self.col_list:
            col_input = input("Type 'y' if you want to create a collection and 'n' if not.")
            if col_input.lower() == 'y':
                self.create.col()
            else:
                print(exit)
                exit()


    def show_sw(self):
        softwares = self.client[self.db][self.col].find()
        for index, software in enumerate(softwares, start = 1):
            print(index, ':', software)

    def insert_sw():
        software_input = "Type name of software."
        
        maker_input = "Type maker of the software."

        Db.show_sw()


    def show_keys():
        number_input = "Type the number of software."


    def insert_key():
        number_input = "Type the number of software."
        insert_key = "Insert a key."

    
    # if db not in db_list:
    #     db_input = input("Type 'yes' if you want to create a database and 'no' if not.")
    #     if db_input == "yes":
    #         #TO DO: CReate Database
    #         db = client[db]
    #         print("Database created!")
    #         #break --> loop?
    #     elif db_input == "no":
    #         #TO DO: QUit program
    #         print(exit)
    #         exit()

    # if col not in col_list:
    #     col_input = input("Type 'yes if you want to create a collection and 'no' if not.")
    #     if col_input == "yes":
    #         #To do: Create collection in SOftware database
    #     else:
    #         #To do: QUIt program
    #         print(exit)
    #         exit()


    
    # #TO DO: Softwares mit Laufnummer anzeigen
    # for db in db_list:
    #     print(db)
    # insert_input = input("Type 'i' if you want to insert a new software, 'k' if you want to show all the key, 'ik' if you want to insert a new key and 'q' if you want to quit the program.")
 


        

