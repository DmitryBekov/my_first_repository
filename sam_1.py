def task1():
    data = input("Введите числа через пробел: ")
    num_list = list(map(int, data.split()))
    num_tuple = tuple(num_list)
    print("Список:", num_list)
    print("Кортеж:", num_tuple)


task1()