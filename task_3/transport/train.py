from .vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, capacity, number_of_cars):
        super().__init__(capacity)
        self.number_of_cars = number_of_cars

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Вагонов: {self.number_of_cars}"