import pprint

trans = {
    1: ['Иванов Иван Иванович','10753229','мастер', '205'],
    2: ['Петров Петр Петрович','1086587','техник', '208'],
    3: ['Родионов Родион Родионович','10753267','инженер', '204'],
    4: ['Федоров Федор Федорович','10753678','начальник отдела', '203'],
    5: ['Васильев Василий Васильевич','10753555','директор', '205'],
}


def inp(txt):
    return input(txt)


def add_word(trans: dict) -> dict:
    z = trans.update({(int(inp('Введите порядковый номер человека: \n'))): [inp('ФИО \n'), inp('Номер телефона: \n'),inp('должность \n'),inp('номер кабинета: \n')]})
    return z


def delete(trans: dict) -> dict:
    while True:
        try:
            del trans[(int(inp('Введите номер сотрудника, которого хотите удалить \n')))]
            return trans
        except KeyError:
            print('Нет такого значения. Введите, то которое есть.')


def search(trans: dict) -> dict:
    while True:
        try:
            z = trans[int(inp('Введите номер сотрудника  \n'))]
            return z
        except KeyError:
            print('Нет такого сотрудника. Введите, того кто есть.')


def vvod(txt):
    while True:
        try:
            vvod = int(input(txt))
            return vvod
        except Exception:
            print('Введите число')


def main(trans):

    vse = 3
    while vse != 0:
        vvo = vvod(
            'Какие операции произвести \n 1-Добавление сотрудника; 2-удаление сотрудника; 3- замена сотрудника; 4 -поиск сотрудника; \n')
        pprint.pprint(trans)
        if vvo == 1:
            add_word(trans)
            pprint.pprint(trans)
        elif vvo == 2:

            delete(trans)
            pprint.pprint(trans)
        elif vvo == 3:

            add_word(trans)
            pprint.pprint(trans)
        elif vvo == 4:
            print(search(trans))

        vse = vvod('Введите любое число, если хотите продолжить, \n Если хотите закончить нажмите 0 ')
        print()


main(trans)
print('Работа завершена!!!')
