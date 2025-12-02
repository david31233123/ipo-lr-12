class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def load(self, weight):
        if weight > self.capacity:
            raise ValueError("Вес превышает вместимость.")
        print(f"Загрузка {weight} кг в {self.name}")

    def __str__(self):
        return f"Транспортное средство: {self.name}, Вместимость: {self.capacity} кг"