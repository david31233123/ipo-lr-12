from .vehicle import Vehicle

class Airplane(Vehicle):
    def __init__(self, name, capacity, range_km):
        super().__init__(name, capacity)
        self.range_km = range_km

    def __str__(self):
        return f"Самолет: {self.name}, Дальность: {self.range_km} км, Вместимость: {self.capacity}"