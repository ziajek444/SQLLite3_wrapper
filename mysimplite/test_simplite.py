from unittest import TestCase, skip
from sqlite3 import *
import os


class TestPylite(TestCase):
    def setUp(self):
        print(80*"- ")
        print("setup:")
        self.data = "xxx"
        self.table_garbage_names = ["dupa.db", "kalosz.db", "123.db"]
        self.db_names = ["test_add_table.db", "test_add_table_fail.db",
                         "test_insert.db", "test_get_filtered_items.db",
                         "test_constructor.db", "test_get_items.db",
                         "test_remove.db", "test_remove_filtered.db",
                         "test_get_table_info.db"]

        files = os.listdir()

        for db_name in self.db_names:
            if db_name in files:
                print("removing", db_name)
                try:
                    os.remove(db_name)
                except Exception as err:
                    print(err)

        print(":all set.")

    def test_constructor(self):
        from simplite import Pylite
        db_name = "test_constructor.db"

        test_db = Pylite(db_name)
        test_db.add_table("tablica_Kota", id="", name="", dupa="")
        test_db.add_table("tablica_Wilka", id="", name="", bomba="")

        print(test_db.get_obj_tables())
        test_db.close_connection()

        test_db = Pylite(db_name)
        test_db.add_table("tablica_Niedzwiedzia", num="", company="", kokosz="")
        test_db.add_table("tablica_Salamandry", counter="", name1="", name2="")

        print(test_db.get_obj_tables())
        test_db.close_connection()

        test_db = Pylite(db_name)
        test_db.close_connection()
        self.assertEqual(1, 1)

    def test_add_table(self):
        from simplite import Pylite
        db_name = "test_add_table.db"
        test_db = Pylite(db_name)
        col_dict=dict()
        col_dict['col_name_1'] = "real"
        col_dict['col_name_3'] = "REAL"
        col_dict['col_name_5'] = "Real"
        col_dict['col_name_7'] = "integer"
        col_dict['col_name_8'] = "INTEGER"
        col_dict['col_name_9'] = "Integer"
        col_dict['col_name_10'] = "text"
        col_dict['col_name_11'] = "TEXT"
        col_dict['col_name_12'] = "Text"

        table_name = ["test_add_table_name"+str(i) for i in range(10)]

        for e in table_name:
            test_db.add_table(e, **col_dict)

        self.assertEqual(test_db.get_tables()[0][0], "test_add_table_name0")
        self.assertEqual(list(test_db.get_colummns(table_name[1])), list(col_dict.keys()))
        self.assertEqual(len(col_dict), len(test_db.get_table_info(table_name[1])))

        test_db.close_connection()
        self.assertEqual(1, 1)

    def test_insert(self):
        from simplite import Pylite
        test_db = Pylite("test_insert.db")
        table_name = "Pracownik"
        test_db.add_table(table_name, id="integer", name="text", surname="text", salary="real", info="")

        test_db.insert(table_name, id="1", name="Marcin", surname="Ziajkowski", salary="40000000.0", info="owsiki")
        test_db.insert(table_name, id="2", name="Kamil", surname="Stoch", salary="10000000.0003", info="1")
        test_db.insert(table_name, id="3", name="Damian", surname="Jakimowocz", salary="41.010003", info="2.3")
        test_db.insert(table_name, id="3", name="Jurek", surname="Kamiński", salary="4100.0")
        test_db.insert(table_name, id="4", name="Kaczor", surname="Donald", salary="1000000000.1000300040005", info="")

        for element in test_db.get_items(table_name):
            print(element)

        test_db.close_connection()
        self.assertEqual(1, 1)

    def test_get_items(self):
        from simplite import Pylite
        test_db = Pylite("test_get_items.db")
        table_name = "Pracownik"
        test_db.add_table(table_name, id="integer", name="text", surname="text", salary="real")

        test_db.insert(table_name, id=66, name="Krystyna", surname="komar", salary=880)
        test_db.insert(table_name, id=77, name="Michalina", surname="Jopek", salary=1750)
        test_db.insert(table_name, salary=2000, name="Ewa", surname="Adam", id=88)
        test_db.insert(table_name, name="Ewa", surname="Nowak", salary=8800, id=1)
        test_db.insert(table_name, name="Ewa", surname="Kołaczkowska", salary=1000, id=2)
        test_db.insert(table_name, name="Karolina", surname="Karo", salary=500, id=3)

        for e in test_db.get_items(table_name):
            print("where=1", e)
        print(8*"  - ")
        for e in test_db.get_items(table_name, "salary < 2000"):
            print("salary < 900", e)
        print(8 * "  - ")
        for e in test_db.get_items(table_name, "name = 'Ewa'"):
            print("name = 'Ewa'", e)
        print(8 * "  - ")
        for e in test_db.get_items(table_name, "id >= 3"):
            print("id >= 3", e)

        test_db.close_connection()
        self.assertEqual(1, 1)

    def test_get_filtered_items(self):
        from simplite import Pylite
        test_db = Pylite("test_get_filtered_items.db")
        table_name = "Pracownik"
        test_db.add_table(table_name, id="integer", name="text", surname="text", salary="real")

        test_db.insert(table_name, id=1, name="Marcin", surname="Komar")
        test_db.insert(table_name, id=66, name="Marcin", surname="komar", salary=880)
        test_db.insert(table_name, id=66, name="Marcin", surname="komar", salary=8900)
        test_db.insert(table_name, id=77, name="Imie2", surname="Jopek")
        test_db.insert(table_name, name="Ewa", surname="Adam", id=88)

        for e in test_db.get_filtered_items(table_name):
            print("no filter", e)
        print(8 * "  - ")
        for e in test_db.get_filtered_items(table_name, id=6):
            print("id=6", e)
        print(8 * "  - ")
        for e in test_db.get_filtered_items(table_name, surname="Ko", salary=8):
            print('surname="Ko", salary=8', e)
        print(8 * "  - ")
        test_db.close_connection()
        self.assertEqual(1, 1)

    def test_remove(self):
        from simplite import Pylite
        test_db = Pylite("test_remove.db")
        table_name = "Pracownik"
        test_db.add_table(table_name, id="", name="", surname="", salary="REAL", city="")
        ids = [str(i+1) for i in range(20)]
        names = ["Adam", "Marcin", "Kamilek", "Ewa", "Kasia"] * 4
        surnames = ["Nowak", "Kowal", "Smith", "Stoh"] * 5
        salaries = [s for s in range(800, 3800, 150)][:20]
        cities = ["London", "Oxenfurt"] * 10
        for i in range(20):
            tmp_dict = dict()
            tmp_dict["id"], tmp_dict["name"] = ids[i], names[i]
            tmp_dict["surname"], tmp_dict["salary"] = surnames[i], salaries[i]
            tmp_dict["city"] = cities[i]
            test_db.insert(table_name, **tmp_dict)

        for element in test_db.get_items(table_name):
            print(element)
        print(8 * "  - ")
        test_db.remove(table_name, "surname='Kowal' and salary>2500")
        for element in test_db.get_items(table_name):
            print(element)

        test_db.close_connection()
        self.assertEqual(1, 1)

    def test_remove_filtered(self):
        from simplite import Pylite
        test_db = Pylite("test_remove_filtered.db")
        table_name = "Pracownik"
        test_db.add_table(table_name, id="", name="", surname="", salary="REAL", city="")
        ids = [str(i + 1) for i in range(20)]
        names = ["Adam", "Marcin", "Kamilek", "Ewa", "Kasia"] * 4
        surnames = ["Nowak", "Kowal", "Smith", "Stoh"] * 5
        salaries = [s for s in range(800, 3800, 150)][:20]
        cities = ["London", "Oxenfurt"] * 10
        for i in range(20):
            tmp_dict = dict()
            tmp_dict["id"], tmp_dict["name"] = ids[i], names[i]
            tmp_dict["surname"], tmp_dict["salary"] = surnames[i], salaries[i]
            tmp_dict["city"] = cities[i]
            test_db.insert(table_name, **tmp_dict)

        for element in test_db.get_items(table_name):
            print(element)
        print(8 * "  - ")
        test_db.remove_filtered(table_name, id=1, name="Ka")
        for element in test_db.get_items(table_name):
            print(element)

        test_db.close_connection()
        self.assertEqual(1, 1)

    @skip("undefined")
    def test_update(self):
        from simplite import Pylite
        test_db = Pylite("test_insert.db")

        test_db.close_connection()
        self.assertEqual(1, 1)

    @skip("undefined")
    def test_get_tables(self):
        from simplite import Pylite
        test_db = Pylite("test_insert.db")

        test_db.close_connection()
        self.assertEqual(1, 1)

    @skip("undefined")
    def test_get_colummns(self):
        from simplite import Pylite
        test_db = Pylite("test_insert.db")

        test_db.close_connection()
        self.assertEqual(1, 1)

    def test_get_table_info(self):
        from simplite import Pylite
        db_name = "test_get_table_info.db"
        test_db = Pylite(db_name)
        col_dict = dict()
        col_dict['col_name_1'] = "real"
        col_dict['col_name_3'] = "REAL"
        col_dict['col_name_5'] = "Real"
        col_dict['col_name_7'] = "integer"
        col_dict['col_name_8'] = "INTEGER"
        col_dict['col_name_9'] = "Integer"
        col_dict['col_name_10'] = "text"
        col_dict['col_name_11'] = "TEXT"
        col_dict['col_name_12'] = "Text"

        table_name = ["test_add_table_name" + str(i) for i in range(10)]

        for e in table_name:
            test_db.add_table(e, **col_dict)

        for e in table_name:
            print(test_db.get_table_info(e))

        test_db.close_connection()
        self.assertEqual(1, 1)


class TestDBFeature(TestCase):
    def setUp(self):
        pass

    def test_6_bit_list(self):
        llll = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                '}', ']', '{', '[', '|', '\\', '+', '_', '=', '-',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
                ';', ':', '<', '>', '/', '?', 'X', 'C', 'V', 'B',
                'N', 'M', ',', '.']
        def conv_10_64(ten:int, min_str_len:int=1) -> str:
            ret = ""
            tmp_l = llll
            ombre = ten
            if ombre == 0:
                return '0'
            while ombre != 0:
                ret = tmp_l[ombre & 0x3f] + ret
                ombre = ombre >> 6
            if len(ret) < min_str_len:
                ret = (min_str_len-len(ret))*'0' + ret

            return ret

        e = 0xEEEFFEEEFF11EEEFFEEEFF11
        mul = 0x32+0x64
        num = 0xff
        for n in range(10, 20):
            num += (mul * n*0x100)
            print(conv_10_64(num, 16), num)
            mul *= 0x32+0x64
        #print(conv_10_64(e), hex(e)[2:])
        #print(conv_10_64(e, 20), hex(e)[2:])
        #print(conv_10_64(e, 40), hex(e)[2:])
        self.assertEqual(1, 1)

    def test_conv_64_10(self):
        llll = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                '}', ']', '{', '[', '|', '\\', '+', '_', '=', '-',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
                ';', ':', '<', '>', '/', '?', 'X', 'C', 'V', 'B',
                'N', 'M', ',', '.']
        def conv_64_10(sf:str) -> int:
            assert(isinstance(sf, str))
            ret = 0
            mul = 64
            gain = 1
            tmp_sf = sf[::-1]
            ll = "".join(llll)
            for e in tmp_sf:
                ret += gain * ll.find(e)
                gain *= mul
            return ret

        e = "BJ.,BKN*BJ.,BKN*"
        print(conv_64_10(e), int("eeeffeeeff11eeeffeeeff11", 16))
        self.assertEqual(conv_64_10(e), int("eeeffeeeff11eeeffeeeff11", 16))
