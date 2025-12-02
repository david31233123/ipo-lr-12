import uuid

class Vehicle:
    def __init__(self, capacity):
        self.vehicle_id = str(uuid.uuid4())
        self.capacity = capacity
        self.current_load = 0
        self.clients_list = []

    def load_cargo(self, client):
        if not hasattr(client, 'cargo_weight'):
            raise TypeError("Объект клиента должен иметь атрибут 'cargo_weight'.")
        cargo_weight = getattr(client, 'cargo_weight')
        if not isinstance(cargo_weight, (int, float)):
            raise TypeError("Значение 'cargo_weight' должно быть числом.")
        if self.current_load + cargo_weight > self.capacity:
            raise ValueError("Груз превышает доступную грузоподъемность.")
        self.current_load += cargo_weight
        self.clients_list.append(client)

    def __str__(self):
        return (f"ID: {self.vehicle_id}, "
                f"Грузоподъемность: {self.capacity} т, "
                f"Текущая загрузка: {self.current_load} т")