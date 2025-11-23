def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(f"{a}\n")
            yield a
            a, b = b, a + b

# Получение 200-го числа Фибоначчи и запись в файл
fib_gen = fib(200)
result = list(fib_gen)[-1]
print(result)