class TransportCompany:
    def __init__(self):
        self.storages = []
        self.clients = []

    def add_storage(self, storage):
        self.storages.append(storage)

    def add_client(self, client):
        self.clients.append(client)

    def distribute_cargo(self):
        # Пример простой логики: распределение по первому доступному транспортному средству
        for client in self.clients:
            loaded = False
            for storage in self.storages:
                for vehicle in storage.vehicles:
                    try:
                        vehicle.load_cargo(client)
                        loaded = True
                        print(f"Загружен {client} в {vehicle}")
                        break
                    except Exception:
                        continue
                if loaded:
                    break
            if not loaded:
                print(f"Не удалось загрузить клиента {client}")

    def optimize_loading(self):
        # Можно добавить алгоритм минимизации ресурсов (например, сортировка по вместимости)
        pass