import os
import os.path

def create_files(path):
    f = open(path,'r', encoding='utf-8')
    cook_book = {}
    try:
        enter = True
        for d in f.read().split("\n"):
            di = {}
            if enter == True:
                tr = []
                cook_book[d]=tr
                sl = d
                enter = False
                continue
            else:
                if len(d.split("|"))>2:
                    di = {'ingredient_name': d.split("|")[0][:-1],'quantity': int(d.split("|")[1]),'measure': d.split("|")[2][1:]}
                    tr.append(di)
                    cook_book[sl] = tr
            if d =="":
                enter = True
        return cook_book
    finally:
        f.close()

def get_shop_list_by_dishes (dishes, person_count):
    recook = create_files("files/recipes.txt")
    dicbf ={}
    for tg in recook:
        if tg in dishes:
            boo = {}
            for gf in recook[tg]:
                dicbf[gf["ingredient_name"]] = {'measure': gf["measure"], 'quantity':int(gf["quantity"])*person_count}
    return dicbf


def st_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

base_path = os.getcwd()
location = os.path.abspath('C:/Users/1/Desktop/Лёша/py-homeworks-basic_files/files_3')
file_for_write = os.path.abspath('C:/Users/1/Desktop/Лёша/py-homeworks-basic_files/files_3/123.txt')
full_path = os.path.join(base_path, location)
def read_file(full_path, file_for_write):
    files = []
    for i in list(os.listdir(full_path)):
        files.append([st_file(os.path.join(full_path, i)), os.path.join(base_path, location, i), i])
    for file_item in sorted(files):
        opening_files = open(file_for_write, 'a', encoding='utf-8')
        opening_files.write(f'{file_item[2]}\n')
        opening_files.write(f'{file_item[0]}\n')
        with open(file_item[1], 'r', encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_item[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()

#print(create_files("files/recipes.txt"))
read_file(full_path, file_for_write)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

