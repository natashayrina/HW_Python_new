def save_names(file_path, sep=","):
    file_path = 'name_file'
    num_names = int(input("Сколько записей Вы хотите внести в телефонную книгу?"))
    myfile = open(file_path, 'w')
    for count in range (1, num_names +1):
        print(f'Введите ФИО №: {count}')
        name = input('ФИО: ')
        talefpon_number = input('Номер телефона: ')
        myfile.write(f'{name}{sep}{talefpon_number}\n')
    print()
    myfile.close()

def write_persons_in_file(file_path, persons, sep=","):
    file_path = 'name_file'
    myfile = open(file_path, 'w')
    for k, v in persons.items():
        myfile.write(f'{k}{sep}{v}\n')
    myfile.close()

def get_records(file_path, sep=","):
    file_path = 'name_file'
    name_file = open(file_path)
    persons = {}
    info = name_file.readlines()
    for i in range(len(info)):
        l = info[i].split(",")
        l[1] = l[1].rstrip("\n")
        persons[l[0]] = l[1]
    name_file.close()
    return persons

def delete_person(file_path, name_for_del, sep=","):
    file_path = 'name_file'
    persons = get_records(file_path, sep)
    #определить что name_for_del в нашем списке persons
    if name_for_del in persons.keys():
        del persons[name_for_del]
    else:
        print("Person not found!")
    write_persons_in_file(file_path, persons)



def update_person(file_path, name_for_update, new_telefon, sep=","):
    file_path = 'name_file'
    persons = get_records(file_path, sep)
    if name_for_update in persons.keys():
       persons [name_for_update] = new_telefon
    else:
        print("Person not found!")

    write_persons_in_file(file_path, persons)

# name_file = input("Введите имя файла - телефонного-справочника")
save_names(file_path = 'name_file')

print(get_records(file_path ='name_file'))
name_for_del = input("Кого Вы хотите удалить из списка?")
delete_person('name_file', name_for_del)
print(get_records(file_path = 'name_file'))

name_for_update = input("Кому нужно изменить номер телефона?")
new_telefon = input(f"Введите новый номер телефона для {name_for_update}")
update_person ('name_file', name_for_update, new_telefon)
print(get_records( 'name_file'))