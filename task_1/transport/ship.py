from .vehicle import Vehicle

class Ship(Vehicle):
    def __init__(self, name, capacity, draft):
        super().__init__(name, capacity)
        self.draft = draft

    def __str__(self):
        return f"Корабль: {self.name}, Осадка: {self.draft}, Вместимость: {self.capacity}"