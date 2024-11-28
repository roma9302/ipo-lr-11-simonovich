from .vehicle import *

class Airplane(Vehicle):
    def init(self, max_altitude, capacity, current_load, clients_list):
        super().init( capacity, current_load, clients_list)
        self.max_altitude = validate_number(max_altitude)
