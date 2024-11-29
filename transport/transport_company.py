from .client import Client
from .vehicle import Vehicle
from .function import *

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_client(self, client):
        self.clients.append(client)

    def output_vehicle(self, client):
        def __str__(self):
            for i in range(len(self.vehicles)):
                return f"{vehicles[i]}"






