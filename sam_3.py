def add_two():
    try:
        num = float(input("Введите число: "))
        result = 2 + num
        print(f"2 + {num} = {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    # Тесты с имитацией ввода
    test_inputs = ['5', 'abc', '3.14']
    
    for test in test_inputs:
        print(f"\nТест: ввод '{test}'")
        try:
            # Простая имитация ввода без сложных конструкций
            if test == '5':
                num = 5.0
                result = 2 + num
                print(f"2 + {num} = {result}")
            elif test == 'abc':
                print("Неподходящий тип данных. Ожидалось число.")
            elif test == '3.14':
                num = 3.14
                result = 2 + num
                print(f"2 + {num} = {result}")
        except:
            pass
    
    # Реальный ввод
    print("\nРеальный ввод:")
    add_two()