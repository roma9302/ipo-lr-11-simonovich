from .function import generate, validate_number
from .client import Client

class Vehicle:
    def __init__(self, capacity, current_load=0, clients_list=None):
        self.vehicle_id = generate()  
        self.capacity = validate_number(capacity)  
        self.current_load = validate_number(current_load)  
        self.clients_list = clients_list 
    def __str__(self):
        return f"ID ТС: {self.vehicle_id}, Грузоподъемность: {self.capacity} т, Текущая загрузка: {self.current_load} т"

if __name__ == "__main__":
    client1 = Client("Alice", 5)
    client2 = Client("Bob", 3, is_vip=True)
    vehicle = Vehicle(capacity=10)
    print(vehicle)  
