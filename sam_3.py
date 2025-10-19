from collections import Counter

def task3(digits_str):
    count = Counter(map(int, digits_str))
    top3 = count.most_common(3)
    sorted_top3 = sorted(top3, key=lambda x: x[0])
    result_dict = dict(top3)
    print("Три самых частых числа (ключ: количество):", result_dict)
    print("Значения в порядке возрастания ключа:", [val for _, val in sorted_top3])
    return result_dict

# Тестирование функции
test_string = "1234567890123456789012345"
print(f"Исходная строка: {test_string}")
task3(test_string)