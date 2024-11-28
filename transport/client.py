from .function import *

class Client: 
    def __init__(self, name, cargo_weight, is_vip=False):
        self.name = validate_str(name)  
        self.cargo_weight = validate_number(cargo_weight)
        self.is_vip = is_vip
