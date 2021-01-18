"""
Задание 4.

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
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

"""
Решение 1. НАЧАЛ, НО НЕ СМОГ ДОДЕЛАТЬ - ПОЖАЛУЙСТА, ПРЕДЛОЖИТЕ СВОЙ ВАРИАНТ КАК ЭТОТ ПУТЬ РЕШЕНИЯ ДОДЕЛАТЬ
"""
""" true - активирован, false - не активирован """

dict_all = {'login1': ['parol1', 'true'],
      'login2': ['parol2', 'false'],
      'login3': ['parol3', 'true'],
      'login4': ['parol4', 'false'],
      'login5': ['parol5', 'true']}
print(dict_all)

key = input("Введите логин пользователя ")
print(key)

def checkKey(dict_all, key):    
    if key in dict_all.keys(): 
        print("User is here.") 
    else: 
        print("User isn't here.") 

checkKey(dict_all, key)



"""
Решение 2. НАЧАЛ, НО НЕ СМОГ ДОДЕЛАТЬ - ПОЖАЛУЙСТА, ПРЕДЛОЖИТЕ СВОЙ ВАРИАНТ КАК ЭТОТ ПУТЬ РЕШЕНИЯ ДОДЕЛАТЬ
"""
""" 1 - активирован, 0 - не активирован """

dict_all = {'login1': ['parol1', 1],
      'login2': ['parol2', 0],
      'login3': ['parol3', 1],
      'login4': ['parol4', 0],
      'login5': ['parol5', 1],
      'key1': ['key', 1]}
print(dict_all)

key = input("Введите логин пользователя ")
print(key)



def checkKey(dict_all, key):
    if key in dict_all: 
        print("Пользователь имеет логин.")
        dict_all = {key: [i1, i2]}
        if i2 = 1
            print("Пользователь активирован.")
        else ("Пройдите активацию.")
            
    else: 
        print("Пользователь не имеет логина.") 

checkKey(dict_all, key)

"""
  ОШИБКА, НАВЕРНОЕ, ГДЕ-ТО ЗДЕСЬ  dict_all = {'key': ['i1', 'i2']}
"""



""" РЕШЕНИЯ ПРЕПОДОВАТЕЛЯ """

# Общая сложность O(n)
def authorization1(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Добро пожаловать! Доступ к ресурсу предоставлен."
            elif value['password'] == user_password and not value['activation']:
                return "Учетная запись не активна! Пройдите активацию!"
            elif value['password'] != user_password:
                return "Пароль не верный."
            
    return "Данного пользователя не существует."


# Общая сложность O(1)
def authorization2(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
                return "Добро пожаловать! Доступ к ресурсу предоставлен."
            elif users[user_name]['password'] == user_password and users[user_name]['activation']:
                return "Учетная запись не активна! Пройдите активацию!"
            elif users[user_name]['password'] != user_password
                return "Пароль не верный."
        else:    
            return "Данного пользователя не существует."


          

















