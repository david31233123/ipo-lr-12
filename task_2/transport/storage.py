class Garage:
    def __init__(self, max_vehicles):
        self.max_vehicles = max_vehicles
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if len(self.vehicles) >= self.max_vehicles:
            raise Exception("Гараж заполнен.")
        self.vehicles.append(vehicle)

    def __str__(self):
        return f"Гараж: {len(self.vehicles)}/{self.max_vehicles} транспортных средств"