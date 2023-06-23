phone_book = {}
path: str = "numbers.txt"


def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    print('\nТелефонная книга успешно загружена!')


def show_contacts(book: dict[int, dict]):
    print('\n' + '=' * 60)
    if book == {}:
        print(f"{'Контакты не найдены!':>40}")
    else:
        for i, contact in book.items():
            new_str = f'{i:>3}. {contact.get("name"):<20}{contact.get("phone"):<20}{contact.get("comment"):<20}'
            print(new_str)
    print('=' * 60 + '\n')


def add_contact():
    uid = max(list(phone_book.keys()))
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid + 1] = {'name': name, "phone": phone, 'comment': comment}

    print(f'\nКонтакт {name} успешно добавлен в книгу!')
    print('=' * 60 + '\n')


def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print(f'Телефонная книга успешно сохранена!')
    print('=' * 60 + '\n')


def search():
    result = {}
    word = input('Введите слово, по которому будет осуществляться поиск:  ')
    for i, contact in phone_book.items():
        if word.lower() in ''.join(list(contact.values())).lower():
            result[i] = contact
    return result


def remove():
    result = search()
    show_contacts(result)
    index = int(input('Введите ID контакта, который хотите удалить: '))
    del_cnt = phone_book.pop(index)
    print(f'Контакт {del_cnt.get("name")} успешно удален!')
    print('=' * 60 + '\n')


def changes():
    result = search()
    show_contacts(result)
    index = int(input('Введите ID контакта, который хотите изменить: '))
    print('Если хотите оставить поле без изменений, нажмите Enter!')
    name = input('Введите новое имя контакта: ')
    phone = input('Введите новый телефон контакта: ')
    comment = input('Введите новый комментарий к контакту: ')

    if name == '':
        pass
    else:
        phone_book[index]['name'] = name
    if phone == '':
        pass
    else:
        phone_book[index]['phone'] = phone
    if comment == '':
        pass
    else:
        phone_book[index]['comment'] = comment

    cng_cnt = phone_book[index]
    print(f'Контакт {cng_cnt.get("name")} успешно изменен!')
    print('=' * 60 + '\n')


def menu() -> int:
    main_menu = ''' Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)

    while True:
        select = input('Введите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        else:
            print('Ошибка ввода. Введите число от 1 до 8')


open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacts(result)
        case 6:
            changes()
        case 7:
            remove()
        case 8:
            print('До свидания!')
            break
