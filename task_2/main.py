from transport.vehicle import Vehicle
from transport.truck import Truck
from transport.storage import Garage
from transport.client import Client
from transport.company import TransportCompany

def main():
    # Создание транспортных средств
    truck1 = Truck(10, "фургон")
    truck2 = Truck(15, "тентованный")
    print(truck1)
    print(truck2)

    # Создание хранилища
    garage = Garage(5)
    garage.add_vehicle(truck1)
    garage.add_vehicle(truck2)

    # Создание клиентов
    client1 = Client("Иван", 3)
    client2 = Client("Мария", 4)
    print(client1)
    print(client2)

    # Создание компании
    company = TransportCompany()
    company.add_storage(garage)
    company.add_client(client1)
    company.add_client(client2)

    # Распределение грузов
    company.distribute_cargo()

if __name__ == "__main__":
    main()