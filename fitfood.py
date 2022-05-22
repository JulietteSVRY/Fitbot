def racion(day_of_the_week):
    filemn = open(f'Рацион похудения/{day_of_the_week}.txt', encoding='utf-8', mode='r')
    list_mn = filemn.readlines()
    filemn.close()
    str = ""
    for string in list_mn:
        str += string
    return str


def racion1(day_of_the_week):
    filemn = open(f'Рацион набора веса/{day_of_the_week}.txt', encoding='utf-8', mode='r')
    list_mn = filemn.readlines()
    filemn.close()
    str = ""
    for string in list_mn:
        str += string
    return str
print(racion1('пн'))
