from transport.client import Client
from transport.vehicle import Vehicle

if __name__ == "__main__":
    client1 = Client("Alice", 50)
    client2 = Client("Bob", 30, is_vip=True)

    vehicle = Vehicle(capacity=100) 

    print(vehicle) 

  
