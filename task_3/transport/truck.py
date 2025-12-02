from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity, color):
        super().__init__(capacity)
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Цвет: {self.color}"