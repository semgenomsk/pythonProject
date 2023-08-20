"""
Задание №8
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей
"""

data = {"Василий": ("спальник", "котелок"),
        "Петр": ("спальник", "котелок", "топор"),
        "Александр": ("спальник", "котелок", "топор", "спирт"),
        "Андрей": ("спальник", "спирт", "палатка")}

# Ищем вещи, которые взяли все.
items_in_common = set.intersection(*(set(items) for items in data.values()))
print("Вещь которую взяли все: ", *items_in_common)

# Ищем уникальные вещи.
lst = []
for k, v in data.items():
    lst.append(set(v))
temp = set()
res_unic = set()
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j:
            temp.update(lst[j])
    temp = lst[i] - temp
    res_unic.update(temp)
    temp = set()
print("Уникальная вещь, которая есть только у одного друга: ", *res_unic)

# Ищем вещь, которая отсутствует только у одного.
for key_name, items in data.items():
    friends = set.intersection(*[set(item) for key, item in data.items() if key != key_name])
    out_items = friends - set(items)
    if out_items:
        print(f"У {key_name} нет вещи, которая есть у всех: ", *out_items)