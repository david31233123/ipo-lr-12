from .storage import Storage

class Port(Storage):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def __str__(self):
        return f"Порт: {super().__str__()}"