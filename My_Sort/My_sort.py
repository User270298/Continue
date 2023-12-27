#Сортировка показаний счетчика:
#1.Сначала сортируются первые занчения
#2.Если первые значения равны- сортируются значения на позиции 3
lst_1 = [
    "827324 gfdgr 2389",
    "827342 ifjedj 9889",
    "827359 rgrgr 9889",
    "827379 gfdgr 9900",

]
lst_2 = [
    "827359 ifjedj 9789",
    "827386 ifjedj 9989"
]


def new_lst(ls: list) -> list:
    lst = []
    for i in ls:
        lst.append(i.split())
    return lst


lst_1 = new_lst(lst_1)
lst_2 = new_lst(lst_2)


def merge(lst_1: list, lst_2: list) -> list:
    res = []
    i = j = 0
    while i < len(lst_1) and j < len(lst_2):
        if int(lst_1[i][0]) < int(lst_2[j][0]):
            res.append(lst_1[i])
            i += 1
        elif int(lst_1[i][0]) > int(lst_2[j][0]):
            res.append(lst_2[j])
            j += 1
        elif int(lst_1[i][0]) == int(lst_2[j][0]):
            if int(lst_1[i][2]) < int(lst_2[j][2]):
                res.append(lst_1[i])
                i += 1
            elif int(lst_1[i][2]) > int(lst_2[j][2]):
                res.append(lst_2[j])
                j += 1
    while i < len(lst_1):
        res.append(lst_1[i])
        i += 1
    while j < len(lst_2):
        res.append(lst_2[j])
        j += 1
    return res


def convert(lst: list) -> list:
    res = []

    for i in range(len(lst)):
        res.append(' '.join(lst[i]))
    return res


print(convert(merge(lst_1, lst_2)))
