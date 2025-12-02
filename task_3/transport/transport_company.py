from .vehicle import Vehicle  # Импортируем класс Vehicle

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Можно добавлять только объекты типа Vehicle.")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return self.vehicles

    def add_client(self, client):
        self.clients.append(client)

    def optimize_cargo_distribution(self):
        # Сортировка клиентов: VIP-клиенты в первую очередь
        clients_sorted = sorted(self.clients, key=lambda c: c.vip, reverse=True)
        # Сортировка транспортных средств по возрастанию вместимости
        self.vehicles.sort(key=lambda v: v.capacity)

        for client in clients_sorted:
            loaded = False
            for vehicle in self.vehicles:
                try:
                    vehicle.load_cargo(client)
                    print(f"Клиент {client.name} загружен в транспорт {vehicle.vehicle_id}")
                    loaded = True
                    break
                except (ValueError, TypeError):
                    continue
            if not loaded:
                print(f"Не удалось загрузить клиента {client.name}")