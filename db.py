import os
import pymongo

class Db():
    
    def __init__(self):
        self.connectionstring = "mongodb+srv://dbadmin:12345@cluster0.iwbd6oa.mongodb.net/?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(self.connectionstring)
        self.db = self.client["Softwares"]
        self.col = self.db["Keys"]
        self.db_list = self.client.list_database_names()

    def create_db_col(self):
        if self.db not in self.db_list:
            db_input = input("No database and collection found. Press 'y' if you want to create one and 'n' if not.")
        else:
            if db_input.lower() == "y":
                self.db = self.client["Softwares"]
                self.col = self.db["Keys"]
                print("Database and collection created.")
            else:
                print("Program ended.")
                exit()


    def show_sw(self):
        print("All the softwares in the database:")
        softwares = list(self.col.find())
        for index, software in enumerate(softwares, start=1):
            print(f"{index} :  {software['name']}")

    def insert_sw(self):
        software_input = input("Type name of software.")
        maker_input = input("Type maker of the software.")
        software = {"name" : software_input, "maker" : maker_input, "keys" : []}
        self.col.insert_one(software)
        print("Software added!:)")


    def show_keys(self):
        number_input = int(input("Type the number of software.")) -1
        software = self.col.find()[number_input]
        keys = software.get("keys", [])
        print("Keys:")
        for key in keys:
            print(key)
        

    def insert_key(self):
        number_input = int(input("Type the number of software.")) -1
        insert_key = input("Insert a key:")
        software = self.col.find()[number_input]
        software_name = software["name"]
        self.col.update_one({"name": software_name}, {"$set": {"keys" : insert_key}})
        print("Added key.")


    