from function import generate, validate_number
from client import Client

class Vehicle:
    def __init__(self, capacity, current_load=0, clients_list=[]):
        self.vehicle_id = generate() 
        self.capacity = validate_number(capacity)  
        self.current_load = validate_number(current_load) 
        self.clients_list = clients_list 

    def load_cargo(self, client):
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Превышение грузоподъемности транспортного средства.")
        
        self.current_load += client.cargo_weight
        self.clients_list.append(client)

    def __str__(self):
        return f"ID ТС: {self.vehicle_id}, Грузоподъемность: {self.capacity} т, Текущая загрузка: {self.current_load} т"


if __name__ == "__main__":
    client1 = Client("Alice", 5)
    client2 = Client("Bob", 1, is_vip=True)

    vehicle = Vehicle(capacity=10)

    print(vehicle.current_load)  

    try:
        vehicle.load_cargo(client1)  
    except ValueError as e:
        print(e)

    try:
        vehicle.load_cargo(client2)  
    except ValueError as e:
        print(e)

    print(vehicle)


    print("Список клиентов в транспортном средстве:")
    for client in vehicle.clients_list: 
        print(f"Клиент: {client.name}, Груз: {client.cargo_weight} т, VIP: {client.is_vip}")
