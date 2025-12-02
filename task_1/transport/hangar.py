from .storage import Storage

class Hangar(Storage):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def __str__(self):
        return f"Ангар: {super().__str__()}"