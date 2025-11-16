class TooYoungError(Exception):
    pass

class InvalidInputError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise TooYoungError("Возраст меньше 18")
    return True

def validate_number(value):
    if not isinstance(value, (int, float)):
        raise InvalidInputError("Требуется число")
    return True

if __name__ == '__main__':
    # Тест первого исключения
    ages = [20, 16, 25]
    for age in ages:
        try:
            check_age(age)
            print(f"Возраст {age} - OK")
        except TooYoungError as e:
            print(f"Ошибка: {e}")
    
    # Тест второго исключения
    values = [10, "текст", 3.14]
    for val in values:
        try:
            validate_number(val)
            print(f"Значение {val} - OK")
        except InvalidInputError as e:
            print(f"Ошибка: {e}")