from simplite import *
import os


if __name__ == '__main__':
    os.remove("baza1.db")
    db = Pylite("baza1.db")

    # Add table
    # first argument is table name.
    # other arguments have to be labeled names equal to data type.for example title="text" or id="int"
    # def add_table(self, table_name, **columns):
    db.add_table("Pracownik", id="integer", name="text", surname="text", salary="real")


    # insert data
    # first argument is table name
    # other arguments have to be a list of args of table column.
    # def insert(self, table_name, *data):
    db.insert("Pracownik", "1", "Marcin", "Ziajkowski", "40000000.0")
    db.insert("Pracownik", "2", "Kamil", "Stoch", "10000000.0003")
    db.insert("Pracownik", "3", "Damian", "Jakimowocz", "41.010003")
    db.insert("Pracownik", "3", "Jurek", "Kamiński", "4100.0")
    db.insert("Pracownik", "4", "Kaczor", "Donald", "1000000000.1000300040005")


    # get items from db
    # first argument is table name
    # second argument is condition
    # def get_items(self, table_name, where=1):
    print("GET before change:")
    print(db.get_items("Pracownik"))


    # remove items
    # first argument is table name
    # second argument is condition
    # def remove(self, table_name, where="1"):
    db.remove("Pracownik", 'name="Damian"')


    # update items values
    # first argument is table name
    # second argument is condition
    # third argument is dictionary of table column names and values
    # def update(self, table_name, where, **columns):
    db.update("Pracownik", 'name="Kaczor"', surname="Tusk")


    print("GET after change:")
    print(db.get_items("Pracownik"))

    print("GET id=3:")
    print(db.get_items("Pracownik", 'id="3"'))

    db.insert("Pracownik", "10", "Amazon", "Dukat", "100.0")
    db.insert("Pracownik", "11", "Amroży", "Funt", "0.0")
    db.insert("Pracownik", "12", "Ambiwalentny", "Goryl", "31.1")
    db.insert("Pracownik", "13", "Ambasador", "Rubel", "41.5")
    print("filtered get:")
    print(db.get_filtered_items("Pracownik", id=1, name="Am", salary="0"))

    print("Get table info")
    print(db.get_colummns("Pracownik"))

    db.close_connection()

'''
    print("Maria")
    maria = LocalDB("Klient", "ID", "name", "surname", "company", "referal")
    print(f"columns in {maria.get_table_name()}")
    print(maria.get_columns())

    maria.add_item(name="Gruby", surname="Nik", ID=90, referal="123-234", company="Coca-Cola")
    maria.add_item(name="Hudy", surname="Kapelusznik", ID=23, referal="124-024", company="Pepszi")
    maria.add_item(name="Gargamel", ID=2, referal="111-000")

    dupa = {"name": "Dzidek", "surname": "Dziobalski", "ID": 34, "referal": "125-356"}
    maria.add_item(**dupa)



    print(maria.get_items())
'''




