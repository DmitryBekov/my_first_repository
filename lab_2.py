class IceCream:
    def __init__(self, topping=None, base_price=100):
        self.base_price = base_price
        if isinstance(topping, str):
            self.topping = topping
            self.price = self.base_price + 20
        else:
            self.topping = None
            self.price = self.base_price

    def show_info(self):
        if self.topping:
            print(f"Мороженое с {self.topping}. Цена: {self.price} руб.")
        else:
            print(f"Обычное мороженое. Цена: {self.price} руб.")

# Пример использования
ice = IceCream("шоколад", 80)
ice.show_info()
