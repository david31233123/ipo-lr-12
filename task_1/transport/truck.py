from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, name, capacity, license_plate):
        super().__init__(name, capacity)
        self.license_plate = license_plate

    def __str__(self):
        return f"Грузовик: {self.name}, Номер: {self.license_plate}, Вместимость: {self.capacity}"