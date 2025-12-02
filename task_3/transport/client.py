class Client:
    def __init__(self, name, cargo_weight, vip=False):
        self.name = name
        self.cargo_weight = cargo_weight
        self.vip = vip  # vip-клиент (по приоритету)

    def __str__(self):
        status = "VIP" if self.vip else "Обычный"
        return f"Клиент: {self.name}, Груз: {self.cargo_weight} т, Статус: {status}"