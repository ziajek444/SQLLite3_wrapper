# -*- coding: utf-8 -*-
"""
    pylite
    ~~~~~~~~~
    :copyright: (c) 2014 by Dariush Abbasi.
    :license: MIT, see LICENSE for more details.
"""

import sqlite3


# Interact with sqlite3 in python as simple as it can be.
class Pylite:
    __SQLite_types = ["", "NULL", "INTEGER", "REAL", "TEXT", "BLOB"]

    # first argument is name of database that store in same name file on disk
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.__tables = dict()
        tt = [x[0] for x in self.get_tables()]
        for table_name in tt:
            self.__tables[table_name] = list(self.get_colummns(table_name))


    # Add table
    # first argument is table name.
    # other arguments have to be labeled names equal to data type.for example title="text" or id="int"
    def add_table(self, table_name, **columns):
        _cols = ""
        for col_name, col_type in columns.items():
            assert str(col_type).upper() in self.__SQLite_types, f"invalid type: {col_type}"
            _cols += col_name + " " + col_type + ","
        _cols = _cols[0:len(_cols) - 1]

        try:
            self.db.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table_name, _cols))
            self.db.commit()
        except Exception as err:
            print(err)
            raise err
        self.__tables[table_name] = list(self.get_colummns(table_name))


    # improved insert
    # insert data
    # first argument is table name
    # other arguments have to be a list of args of table column.
    def insert(self, table_name, **data):
        new_values = list()
        tmp_columns = list(self.get_colummns(table_name))
        columns_amount = len(tmp_columns)
        cols_string = ""
        for col, value in data.items():
            assert col in tmp_columns, f"{col} is not valid columns"
            new_values.append('"' + str(value) + '"')
            tmp_columns.remove(col)
            cols_string += f"{col}, "
        for missing_col in tmp_columns:
            new_values.append('"-"')
            cols_string += f"{missing_col}, "
        cols_string = cols_string[:-2]
        new_values = ",".join(new_values)

        command_str = f"INSERT INTO {table_name} ({cols_string}) values({new_values})"

        self.db.execute(command_str)
        self.db.commit()

    # get items from db
    # first argument is table name
    # second argument is condition
    def get_items(self, table_name, where=1):
        _items = self.db.execute("SELECT * FROM {} WHERE {}".format(table_name, where))
        self.db.commit()
        return list(_items)

    def get_filtered_items(self, table_name, **filters):
        _filtered_items_cmd = "SELECT * FROM {} WHERE ".format(table_name)
        for col, filter in filters.items():
            _filtered_items_cmd += f'(lower({col}) LIKE "{str(filter)}%") AND '
        _filtered_items_cmd = _filtered_items_cmd[0:-4]
        _filtered_items = self.db.execute(_filtered_items_cmd)
        return list(_filtered_items)


    # remove items
    # first argument is table name
    # second argument is condition
    def remove_filtered(self, table_name, **filters):
        _filtered_items_cmd = "DELETE FROM {} WHERE ".format(table_name)
        for col, filter in filters.items():
            _filtered_items_cmd += f'(lower({col}) LIKE "{str(filter)}%") AND '
        _filtered_items_cmd = _filtered_items_cmd[0:-4]
        self.db.execute(_filtered_items_cmd)
        self.db.commit()

    # remove items
    # first argument is table name
    # second argument is condition
    def remove(self, table_name, where="1"):
        self.db.execute("DELETE FROM {} WHERE {}".format(table_name, where))
        self.db.commit()


    # update items values
    # first argument is table name
    # second argument is condition
    # third argument is dictionary of table column names and values
    def update(self, table_name, where, **columns):
        _cols = ""
        for col_name, col_type in columns.items():
            _cols += col_name + ' = "' + col_type + '",'
        _cols = _cols[0:len(_cols) - 1]

        self.db.execute("UPDATE {} SET {} where {}".format(table_name, _cols, where))

    # return list of tables
    def get_tables(self):
        _tables = self.db.execute("SELECT name FROM sqlite_master")
        return list(_tables)

    def get_colummns(self, table_name):
        table_info = self.get_table_info(table_name)
        table_columns = tuple([element[1] for element in table_info])
        return table_columns

    def get_obj_tables(self):
        return self.__tables

    def get_table_info(self, table_name):
        return self.query(f"PRAGMA table_info('{table_name}') ").fetchall()

    # execute sqlite query's
    def query(self, query_string):
        ret = self.db.execute(query_string)
        self.db.commit()
        return ret

    def __repr__(self):
        # ret = "\t\t|\t\t".join([x for x in self.__columns])
        # for row in self.__items:
        #     ret += "\n"
        #     for col_name in self.__columns:
        #         ret += f"{row[col_name]}\t\t|\t\t"
        # return ret
        pass

    def __getitem__(self, item):
        # return self.__items[item]
        pass

    # close database connection
    def close_connection(self):
        self.db.close()


'''
class LocalDB:
    def __init__(self, table_name:str, *columns):
        self.__table_name = table_name
        self.__columns = set()
        for col in columns:
            assert(isinstance(col, str))
            self.__columns.add(col)
        self.__columns = tuple(self.__columns)
        self.__items = list()

    def add_item(self, **data):
        new_item = dict()
        tmp_columns = list(self.__columns)
        for col, value in data.items():
            assert col in tmp_columns, f"{col} is not valid columns"
            new_item[col] = value
            tmp_columns.remove(col)
        for missing_col in tmp_columns:
            new_item[missing_col] = None
        assert (len(new_item) == len(self.__columns))
        self.__items.append(new_item)

    def get_items(self):
        return self.__items

    def get_filtered_items(self, **filter):
        """ obj.get_filtered_items(col_name1="abc") col_name1 start with "abc"
            obj.get_filtered_items(col_name1=2) col_name1 start with "2"
            obj.get_filtered_items(col_name1=4.201) col_name1 start with "4.201"
            obj.get_filtered_items(col_name1=2, col_name2="B") col_name1 -> "2" AND col_name2 -> "B"
            """

        return self.__items

    def __getitem__(self, item):
        return self.__items[item]

    def get_columns(self):
        return self.__columns

    def get_table_name(self):
        return self.__table_name

    def __repr__(self):
        ret = "\t\t|\t\t".join([x for x in self.__columns])
        for row in self.__items:
            ret += "\n"
            for col_name in self.__columns:
                ret += f"{row[col_name]}\t\t|\t\t"
        return ret
'''



















