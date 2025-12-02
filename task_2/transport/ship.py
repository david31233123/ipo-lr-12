from .vehicle import Vehicle

class Ship(Vehicle):
    def __init__(self, capacity, port):
        super().__init__(capacity)
        self.port = port

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Порт: {self.port}"