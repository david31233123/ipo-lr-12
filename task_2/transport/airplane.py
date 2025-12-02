from .vehicle import Vehicle

class Airplane(Vehicle):
    def __init__(self, capacity, airline):
        super().__init__(capacity)
        self.airline = airline

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Авиакомпания: {self.airline}"