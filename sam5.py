from collections import Counter

def task5():
    list_1 = [1, 1, 3, 3, 1]
    list_2 = [5, 5, 5, 5, 5, 5, 5, 5]
    list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
    
    def transform_list(lst):
        result_set = set()
        counter = Counter(lst)
        for num, count in counter.items():
            result_set.add(num)
            for k in range(2, count + 1):
                result_set.add(str(num) * k)
        return result_set
    
    print("Задание 5:")
    print(f"Множество 1: {transform_list(list_1)}")
    print(f"Множество 2: {transform_list(list_2)}")
    print(f"Множество 3: {transform_list(list_3)}")

task5()