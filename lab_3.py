class Secret:
    def __init__(self, value):
        self.__hidden = value  # инкапсуляция (приватный атрибут)
        print("Объект создан.")

    def get_value(self):
        return self.__hidden

    def set_value(self, new_value):
        self.__hidden = new_value
        print("Значение обновлено.")

    def __del__(self):
        print("Объект удален.")

# Пример использования
obj = Secret("секрет")
print(obj.get_value())
obj.set_value("новый секрет")
print(obj.get_value())

# Ошибка при прямом обращении:
# print(obj.__hidden)  # AttributeError
