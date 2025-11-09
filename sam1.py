class Gardener:
    @staticmethod
    def knowledge_base():
        print("""
        Справка по садоводству:
        1. Томаты растут постепенно, проходя стадии: отсутствует → цветение → зелёный → красный.
        2. Ухаживайте за растениями, пока все томаты не созреют.
        3. Урожай можно собирать только после полного созревания.
        """)

# Тест №1 — вызов справки
Gardener.knowledge_base()


class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зелёный', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        self.print_state()

    def is_ripe(self):
        return self._state == 3

    def print_state(self):
        print(f"Томат {self._index}: стадия — {Tomato.states[self._state]}")



class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        print("\nКуст растёт...")
        for tomato in self.tomatoes:
            tomato.grow()
    
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        print("Урожай собран!\n")
        self.tomatoes = []



class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"\n{self.name} ухаживает за растением...")
        self._plant.grow_all()
        print(f"{self.name} закончил работу.")
    
    def harvest(self):
        print(f"\n{self.name} проверяет урожай...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собрал урожай! 🍅")
        else:
            print("Рано собирать — томаты ещё не все спелые!")



# Создаём куст и садовника
bush = TomatoBush(3)
gardener = Gardener("Михаил", bush)

# Уход №1
gardener.work()
gardener.harvest()  # Рано собирать

# Уход №2
gardener.work()
gardener.harvest()  # Ещё не все спелые

# Уход №3
gardener.work()
gardener.harvest()  # Томаты дозрели — урожай собран
