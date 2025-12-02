from transport.truck import Truck
from transport.ship import Ship
from transport.airplane import Airplane
from transport.garage import Garage
from transport.port import Port
from transport.hangar import Hangar
from transport.company import TransportCompany
from transport.client import Client

def main():
    company = TransportCompany()

    garage = Garage("Центральный гараж", 3)
    port = Port("Главный порт", 2)
    hangar = Hangar("Аэропорт", 2)

    company.add_storage(garage)
    company.add_storage(port)
    company.add_storage(hangar)

    truck1 = Truck("Грузовик 1", 5000, "A123BC")
    ship1 = Ship("Корабль 1", 10000, 15)
    airplane1 = Airplane("Самолет 1", 2000, 3000)

    garage.add_vehicle(truck1)
    port.add_vehicle(ship1)
    hangar.add_vehicle(airplane1)

    client1 = Client("Иван", 3000)
    client2 = Client("Анна", 6000, True)

    company.add_client(client1)
    company.add_client(client2)

    company.optimize_load()

if __name__ == "__main__":
    main()