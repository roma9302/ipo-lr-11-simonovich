from transport.client import Client
from transport.van import Van 
from transport.airplane import Airplane
from transport.transport_company import TransportCompany
from transport.vehicle import *
from transport.hangar import Hangar
import json

close = True
company = TransportCompany("Транспортная компания")


def add_client():
    name = input("Введите имя клиента: ")
    cargo_weight = input("Введите вес груза: ")
    is_vip = input("VIP клиент (да/нет): ").lower() == "да"
    
    if validate_str(name) != None and validate_number(cargo_weight) != None: #Валидация если функция возвращает не  None , то возврашаем значения, нет -> в файл не сохраняется клиент
        client = Client(name, cargo_weight, is_vip) #Класс клиента
        company.add_client(client)




def add_vehicle():
    counter = 0 #Счетчик количества т/с в т/к
    try:
        
        with open("transport/database.json", 'r', encoding='utf-8') as file:
            vehicles_data = json.load(file)
            
            for a in vehicles_data['fields']['vehicles']:
                counter += 1 #подсчет т/с
                
            if vehicles_data['fields'].get('hangars', 0) - 1 >= counter: 
                vehicle_type = input("Введите тип (van/airplane): ")
                capacity = input("Введите грузоподъемность: ")
                
                if validate_number(capacity) is not None:
                    if vehicle_type.lower() == "van":
                        is_refrigerated =  input("Холодильник (да/нет): ")
                        van = Van(is_refrigerated, capacity, 0, []) #Класс Фургон
                        company.add_vehicle(van)
                        
                    elif vehicle_type.lower() == "airplane":
                        max_altitude = input("Введите максимальную высоту: ")
                        
                        if validate_number(max_altitude) is not None:
                            airplane = Airplane(max_altitude, capacity, 0, []) #Класс аироплан
                            company.add_vehicle(airplane)
                            
                        else:
                            print("Макимальная высота должна принимать целочисленное/дробное значение")
                else:
                    print("Грузоподьемность должна принимать значение целочисленное/дробное")
            else:
                print("мест в ангаре нет.")
    except:
        print(f"Ошибка при создании т/с")


#Выход из программы(смена флага True на False)
def leave():
    global close
    print("Программа завершена. Можно в любой момент вернуться к текущей базе клиентов/транспорта")
    close = False 



#Остальные функции в #Функции в файле function.py
def console_programm():
    while close:
        try:
            menu()
            num = int(input("Выберите вариант взаимодействия "))
            if num == 1:
                Hangar.hangar_menu()
            elif num == 2:
                add_client()
            elif num == 3:
                add_vehicle()
            elif num == 4:
                output_client()
            elif num == 5:
                output_completed_client()
            elif num == 6:
                company.list_vehicles()
            elif num == 7:
                company.optimize_cargo_distribution()
            elif num == 8:
                Vehicle.load_cargo(0)
            elif num == 9:
                unloading_caro() 
            elif num == 10:
                example()
            elif num == 11:
                leave()
            else:
                print("Ошибка. Выберите От 1 до 11 ")
        except:
            print("Непредвиденная ошибка. Попробуйте еще раз ")

        
console_programm()

