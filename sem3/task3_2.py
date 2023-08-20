"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов
"""

lst = [11, 1, 12, 12, 34, 1, 22, 447, 123, 22, 112, 1]

lst_unc = []
for el in lst:
    if lst.count(el) > 1:
        lst_unc.append(el)
print(list(set(lst_unc)))

# или
# lst_new = []
# for el in lst:
#     if lst.count(el) > 1 and el not in lst_new:
#         lst_new.append(el)
# print(lst_new)