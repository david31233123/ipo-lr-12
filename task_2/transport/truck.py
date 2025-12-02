from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity, truck_type):
        super().__init__(capacity)
        self.truck_type = truck_type  # Например, 'тентованный', 'фургон', и т.д.

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Тип: {self.truck_type}"