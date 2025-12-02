from .garage import Garage
from .port import Port
from .hangar import Hangar
from .client import Client

class TransportCompany:
    def __init__(self):
        self.storages = []
        self.clients = []

    def add_storage(self, storage):
        self.storages.append(storage)

    def add_client(self, client):
        self.clients.append(client)

    def optimize_load(self):
        # Простая оптимизация для примера
        for client in self.clients:
            print(f"Обработка клиента: {client.name} с грузом {client.cargo_weight} кг.")
            for storage in self.storages:
                for vehicle in storage.contents:
                    try:
                        vehicle.load(client.cargo_weight)
                        print(f"Груз {client.cargo_weight} кг загружен в {vehicle.name}.")
                        break
                    except ValueError:
                        continue

    def __str__(self):
        return f"Компания с {len(self.storages)} хранилищами и {len(self.clients)} клиентами"