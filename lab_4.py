class Mammal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"{self.name} — млекопитающее.")

class Cat(Mammal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def describe(self):
        print(f"{self.name} — кошка цвета {self.color}, она млекопитающее.")

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def describe(self):
        print(f"{self.name} — собака породы {self.breed}, она млекопитающее.")

# Пример использования
cat = Cat("Мурка", "белого")
dog = Dog("Бобик", "овчарка")
cat.describe()
dog.describe()
