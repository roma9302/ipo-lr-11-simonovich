from .vehicle import *

class Van(Vehicle):
    def init(self, is_refrigerated , capacity, current_load, clients_list):
        super().init( capacity, current_load, clients_list)
        self.is_refrigerated = True if is_refrigerated.lower() == "да" else False
