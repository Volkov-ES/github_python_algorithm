"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

"""
ЗАПАС КОДА
import operator

my_dict = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(my_dict)

max3_dict = max(my_dict.items(), key = operator.itemgetter(1))[0]

print(max3_dict)
"""
"""
ЗАПАС КОДА
my_dict = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(my_dict)

max_val = max(my_dict.values())
final_dict = {k:v for k, v in my_dict.items() if v == max_val}

print(final_dict)

"""



"""
Решение №1 (через сортировку) - O(N*log N)
"""

my_dict = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(my_dict)

max_dict3 = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

print(max_dict3)

for val in max_dict3:

    print(val, ":", my_dict.get(val))

print('#' *18)

"""
Решение №2 (через использование heapq.nlargest()) - O(N)
"""

from heapq import nlargest

my_dict = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(my_dict)

three_highest = nlargest(3, my_dict, key = my_dict.get)

print(three_highest)


for val in three_highest:

    print(val, ":", my_dict.get(val))

print('#' *18)

"""
Решение №3 (через from collections import Counter) - O(N)
"""

from collections import Counter

my_dict = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(my_dict)

k = Counter(my_dict)
high_3 = k.most_common(3)

print(high_3)

for i in high_3:

    print(i[0]," :",i[1]," ")

print('#' *18)

""" Лучшими вариантами будут второй и третий, так как имеют минимальную выяислительную сложность
и решают поставленную задачу без изменения исходного словаря и без лишней сортировки. """


""" РЕШЕНИЯ ПРЕПОДОВАТЕЛЯ """

# первый вариант - O(n^2)
base_company = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(base_company)

def sorted_1(random_list):
    for i in range(len(random_list)):
        lowest_value_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_value_index][1]:
                lowest_value_index = j
        random_list[i], random_list[lowest_value_index] = random_list[lowest_value_index], random_list[i]
    return random_list[0:3]

list_from_dictionary = list(base_company.items())
for i in sorted_1(list_from_dictionary):
    print(i[0], ':', i[1])
    
print('#' *18)


# второй вариант - O(N*log N)
base_company = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(base_company)

list_from_dictionary = list(base_company.items())
list_from_dictionary.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_from_dictionary[i][0], ':', list_from_dictionary[i][1])

print('#' *18)


# третий вариант - O(N)
base_company = {'VTB': 1200, 'ROSTELECOM': 4500, 'SBERBANK': 17000, 'LUKOIL': 17000, 'MAGNIT': 3500, 'GAZPROM': 25000, 'SEVERSTAHL': 6000}
print(base_company)

def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max

print(three_max(base_company))

""" Лучшим вариантом будет третий, так как имеет минимальную выяислительную сложность
и решает поставленную задачу без изменения исходного словаря и без лишней сортировки. """


