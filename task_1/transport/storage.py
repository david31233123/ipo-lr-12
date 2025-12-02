class Storage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.contents = []

    def add_vehicle(self, vehicle):
        if len(self.contents) >= self.capacity:
            raise ValueError(f"{self.name} переполнен.")
        self.contents.append(vehicle)

    def __str__(self):
        return f"{self.name}: {len(self.contents)}/{self.capacity} занято"