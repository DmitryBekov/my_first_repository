class Introduce:
    def __init__(self, name, guess):
        self.name = name
        if guess == self.name:
            print("Вы угадали мое имя!")
        else:
            print("Нет, это не мое имя.")
        
        # Проверка несуществующего атрибута
        try:
            print(self.surname)
        except AttributeError:
            print("Атрибут 'surname' не существует в этом классе.")

# Пример использования
person = Introduce("Михаил", "Иван")
