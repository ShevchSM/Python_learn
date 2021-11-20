####################################################################################################
import random

# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.


def modified_list(list_input01):
    list_output01 = []
    for item01 in range(len(list_input01)):
        if item01 % 2:
            list_output01.append(list_input01[item01][::-1])
        else:
            list_output01.append(list_input01[item01])
    return list_output01


my_list01 = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
print("|1.|>>>", modified_list(my_list01))

# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".


def modified_list_first_symbol(list_input02):
    list_output02 = []
    for item02 in range(len(list_input02)):
        if str(list_input02[item02]).startswith('a'):
            list_output02.append(str(list_input02[item02]))
    return list_output02


my_list02 = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
print("|2.|>>>", modified_list_first_symbol(my_list02))


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

def modified_list_find_symbol(list_input03):
    list_output03 = []
    for item03 in range(len(list_input03)):
        if "a" in str(list_input03[item03]):
            list_output03.append(str(list_input03[item03]))
    return list_output03


my_list03 = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
print("|3.|>>>", modified_list_find_symbol(my_list03))

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

def modified_list_from_str(list_input04):
    list_output04 = []
    for str04 in list_input04:
        if isinstance(str04, str):
            list_output04.append(str04)
    return list_output04


my_list04 = [5, 9, "ghi", 10, 15, 25, 30, 32, 95]
print("|4.|>>>", modified_list_from_str(my_list04))

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.


def create_list_from_str(str_input05):
    list_output05 = []
    for symbol05 in set(str_input05):
        if str_input05.count(symbol05) == 1:
            list_output05.append(symbol05)
    return list_output05


my_str05 = "abcdefghijklmnopqrstuvwxyz_abcdefg"
print("|5.|>>>", sorted(create_list_from_str(my_str05)))

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.


def create_list_from_two_str01(str_input061, str_input062):
    list_output06 = []
    for symbol06 in set(str_input061 + str_input062):
        list_output06.append(symbol06)
    return list_output06


my_str061 = "abcdefghijklmnopqr"
my_str062 = "stuvwxyz_abcdefg"
print("|6.|>>>", sorted(create_list_from_two_str01(my_str061, my_str062)))


# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.


def create_list_from_two_str02(str_input071, str_input072):
    list_output07 = set(create_list_from_str(str_input071)).intersection(create_list_from_str(str_input072))
    return list_output07


my_str071 = "abcdefghijklmnopqr"
my_str072 = "stuvwxyz_abc"
print("|7.|>>>", sorted(create_list_from_two_str02(my_str071, my_str072)))


# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com


def create_email(domains_in08, names_in08):
    str_rand08 = ""
    for symbol08 in range(random.randint(5, 7)):
        str_rand08 += chr(random.randint(97, 122))
    email_out08 = f"{random.choice(names_in08)}.{random.randint(100, 999)}" \
                  f"@{str_rand08}.{random.choice(domains_in08)}"
    return email_out08


names = ["king", "miller", "kean", "williams", "peters", "gibson", "martin", "jordan"]
domains = ["net", "com", "ua", "biz", "org", "info"]
e_mail = create_email(domains, names)
print("|8.|>>>", e_mail)

