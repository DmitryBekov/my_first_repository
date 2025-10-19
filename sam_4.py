def slice_between_occurrences(tup, element):
    if element not in tup:
        return ()
    first_index = tup.index(element)
    try:
        second_index = tup.index(element, first_index + 1) + 1
    except ValueError:
        return tup[first_index:]
    return tup[first_index:second_index]

test_cases = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

for tup, elem in test_cases:
    print(f"Кортеж: {tup}, ID: {elem} -> Результат: {slice_between_occurrences(tup, elem)}")