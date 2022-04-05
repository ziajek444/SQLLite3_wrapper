#builds source files with cities names contained in dictionary
# borough -> gmina

from openpyxl import load_workbook
import os

wb = load_workbook(filename ='gminy.xlsx')
sheet_ranges = wb['Gminy']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ref_path_to_main_root = "../"
FROM_ROOT = ref_path_to_main_root

umbrella_file_name = "gminy_baza"
umbrella_file_dir = FROM_ROOT + "built_source/"
umbrella_import_tree = "built_source.gminy."  # full import -> umbrella_import_tree + filename

data_file_dir = FROM_ROOT + "built_source/gminy/"
data_file_start_name = "gminy_baza_"
data_file_import_tree = "built_source."  # full import -> data_file_import_tree + filename

ENCODE = "UTF-8"
main_dict_name = "dict_boroughs"
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## dict_cities = dict()
def create_main_dict():
    with open(f"{umbrella_file_dir}{umbrella_file_name}.py", "bw") as pyfile:
        pyfile.write(f"\n{main_dict_name} = dict()\n\n".encode(ENCODE))


## from built_source.miasta.miasta_baza_100122 import *  ## umbrella
## from built_source.miasta_baza import dict_cities      ## data_file
## dict_cities["ma"] = list()                            ## data_file
def add_new_dict_tag(tag_name):
    # "aaaża" -> 97979738097
    tag_number = "".join([str(ord(x)) for x in tag_name])
    with open(f"{umbrella_file_dir}{umbrella_file_name}.py", "ba") as pyfile:
        pyfile.write(f"from {umbrella_import_tree}{data_file_start_name}{tag_number} import * \n".encode(ENCODE))
    with open(f"{data_file_dir}{data_file_start_name}{tag_number}.py", "bw") as pyfile:
        pyfile.write(f"from {data_file_import_tree}{umbrella_file_name} import {main_dict_name}\n\n".encode(ENCODE))
        pyfile.write(f"{main_dict_name}[\"{tag_name}\"] = list()\n\n".encode(ENCODE))


## dict_cities["ma"].append("Macakówka")
def add_city_name_to_tag(element_name, tag_name):
    # "aaaża" -> 97979738097
    tag_number = "".join([str(ord(x)) for x in tag_name])
    with open(f"{data_file_dir}{data_file_start_name}{tag_number}.py", 'ba') as pyfile:
        pyfile.write(f"\n{main_dict_name}[\"{tag_name}\"].append(\"{element_name}\")\n".encode(ENCODE))


isExist = os.path.exists(data_file_dir)
if not isExist:
    os.makedirs(data_file_dir)

create_main_dict()
all_tags = list()
for city_name in sheet_ranges['A']:
    city_name_str = city_name.value.strip()
    if city_name_str is not None:
        tmp_tag = city_name_str[0:2].lower()
        if tmp_tag in all_tags:
            add_city_name_to_tag(city_name_str, tmp_tag)
        else:
            all_tags.append(tmp_tag)
            add_new_dict_tag(tmp_tag)
            add_city_name_to_tag(city_name_str, tmp_tag)
            print(f"add {tmp_tag}")
    else:
        print("no borough name")

print("done")

''' < built_source/miasta/miasta_baza_10997.py >

from built_source.miasta_baza import dict_cities

dict_cities["ma"] = list()


dict_cities["ma"].append("Macakówka")

dict_cities["ma"].append("Macew")

...
'''


''' < built_source/miasta_baza.py >

dict_cities = dict()

from built_source.miasta.miasta_baza_100122 import * 
from built_source.miasta.miasta_baza_9798 import * 
from built_source.miasta.miasta_baza_9799 import * 
...
'''
