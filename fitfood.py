def racion(day_of_the_week):
    filemn = open(f'Рацион похудения/{day_of_the_week}.txt', encoding='utf-8', mode='r')
    list_mn = filemn.readlines()
    filemn.close()
    str = ""
    for string in list_mn:
        str += string
    return str

