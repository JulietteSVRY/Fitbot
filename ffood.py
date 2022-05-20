import csv
import re

recipes_dictionary = {}  # Словарь для рецептов
weekfood_dictionary = {}  # Словарь рациона питания на неделю

with open('рецепты.csv') as File: #НЕ ПРИВЯЗАЛА ЕЩЕ НОРМАЛЬНО!!!!!!!!!!!!!!!!
    reader = csv.reader(File, delimiter=';', quotechar=',',  # Считываем данные из csv файла
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        # print(row)
        recipes_dictionary[row[0]] = row[3] = row[6] = row[9] # Добавляем в словари
        weekfood_dictionary[row[12]] = row[14] = row[16] = row[18] = row[20] = row[22] = row[24]

############################################################################################
recipes_list = []
for key in recipes_dictionary:  # Первично добавляем позиции рецептов в массив рецептов
    if key != '':
        recipes_list.append(key)

weekfood_list = []         # Первично добавляем позиции недельного рациона в массив недельного питания
for key in weekfood_dictionary:
    if key != '':
        weekfood_list.append(key)
