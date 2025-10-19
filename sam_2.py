def remove_first_occurrence(tup, element):
    lst = list(tup)
    if element in lst:
        lst.remove(element)
    return tuple(lst)


test_cases = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]

for tup, elem in test_cases:
    print(f"Исходный: {tup}, Удалить: {elem} -> Результат: {remove_first_occurrence(tup, elem)}")