class Client:
    def __init__(self, name, cargo_weight):
        self.name = name
        self.cargo_weight = cargo_weight

    def __str__(self):
        return f"Клиент: {self.name}, Груз: {self.cargo_weight} т"