from .storage import Storage

class Garage(Storage):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def __str__(self):
        return f"Гараж: {super().__str__()}"