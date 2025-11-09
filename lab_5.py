class Russian:
    greeting = "Привет"

    @staticmethod
    def say_hello():
        print(f"На русском говорят: {Russian.greeting}")

class English:
    greeting = "Hello"

    @staticmethod
    def say_hello():
        print(f"In English they say: {English.greeting}")

# Демонстрация полиморфизма
for lang in (Russian, English):
    lang.say_hello()
