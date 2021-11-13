####################################################################################################
# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
persons11 = [{"name": "John", "age": 15}, {"name": "Jessy", "age": 15}, {"name": "Jozzy", "age": 17},
             {"name": "Jack", "age": 45}]

# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
sort_age11 = sorted(persons11, key=lambda item: item["age"], reverse=False)
for index11 in sort_age11:
    if index11.get("age") == sort_age11[1].get("age"):
        print("|1) а)|>>>", index11.get("name"))

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
sort_age12 = sorted(persons11, key=lambda item: len(item["name"]), reverse=True)
for index12 in sort_age12:
    if len(index12.get("name")) == len(sort_age12[1].get("name")):
        print("|1) б)|>>>", index12.get("name"))

# в) Посчитать среднее количество лет всех людей из списка.
sum_age = 0
for index13 in persons11:
    sum_age += index13.get("age")
result13 = sum_age/len(persons11)
print("|1) в)|>>>", result13)


####################################################################################################
# 2) Даны два словаря my_dict_1 и my_dict_2.
my_dict21 = {i: i**2 for i in range(1, 10, 2)}
my_dict22 = {i: i**2 for i in range(2, 10, 3)}
print("|2)   |>>>", my_dict21)
print("|2)   |>>>", my_dict22)

# а) Создать список из ключей, которые есть в обоих словарях.
my_list21 = list(set(list(my_dict21)).intersection(list(my_dict22)))
print("|2) а)|>>>", my_list21)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
my_list22 = list(set(list(my_dict21)).difference(list(my_dict22)))
print("|2) б)|>>>", my_list22)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
my_dict23 = {}
for item23 in my_list22:
    my_dict23[item23] = my_dict21.get(item23)
print("|2) в)|>>>", my_dict23)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
my_dict24 = my_dict21
my_dict24.update(my_dict22)
for item24 in my_list21:
    my_dict24.pop(item24)
print("|2) г)|>>>", my_dict24)

# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
my_dict25 = my_dict21
my_dict25.update(my_dict22)
for item25 in my_list21:
    my_dict25[item25] = [my_dict21[item25], my_dict22[item25]]
print("|2) г)|>>>", my_dict25)
