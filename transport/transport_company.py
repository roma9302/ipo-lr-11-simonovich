from .client import Client
from .vehicle import *
from .function import *
import json

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_client(self, client):
        self.clients.append(client)

#Метод для вывода обьектов класса посредством чтения их из файла
    def list_vehicles(self):
        Found = False
        try:
            with open("transport/database.json", 'r', encoding='utf-8') as file:
                vehicles_data = json.load(file)
                
            try:
                vehicles = vehicles_data["fields"]["vehicles"]
            except:
                print("Возникла ошибка при выводе т/с . Их нет")

            #Перебор всех атрибутов обьектов в файле (get дабы избежать ошибок если значения не будет. Т.е для разделения на подклассы)
            print("Доступные Транспортные средства:")
            for vehicle_data in vehicles:
                vehicle_id = vehicle_data['vehicle_id']
                vehicle_type = vehicle_data['type']
                capacity = vehicle_data['capacity']
                current_load = vehicle_data['current_load']
                is_refrigerated = vehicle_data.get('is_refrigerated') 
                max_altitude = vehicle_data.get('max_altitude')
                Found = True
        

                #Вывод фургонов
                if vehicle_type == 'van':
                    print(f"""
                            Тип: {vehicle_type}
                            Айди: {vehicle_id}
                            Грузоподьемность: {capacity}
                            Текущая загруженность: {current_load}
                            Наличие холодильника: {is_refrigerated}
                            """)

                #Вывод аиропланов
                elif vehicle_type == 'airplane':
                    print(f"""
                            Тип: {vehicle_type}
                            Айди: {vehicle_id}
                            Грузоподьемность: {capacity}
                            Текущая загруженность: {current_load}
                            Максимальная высота подьема {max_altitude}
                            """)
            if Found == False:
                print("Нет доступных т/с")
                    
        except:
            print("Ошибка при выводе транспорта. Проверьте его наличие")


    #Метод для оптимизации загрузки данных(не вручную)
    #Вызывает функцию из файла function.py
    def optimize_cargo_distribution(self):
        optimize()


