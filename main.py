from transport.client import Client
from transport.van import Van 
from transport.airplane import Airplane
from transport.transport_company import TransportCompany
from transport.vehicle import *
import json

close = True
company = TransportCompany("Транспортная компания")


def hangar():
    hangar_close = True #Флажок для выхода из доп. меню
    with open("transport/database.json", 'r', encoding='utf-8') as file:
        vehicles_data = json.load(file)
    while hangar_close: 
        
        counter =0 # подсчет количества т/с в т/к (1 ангар - 1 т/с)
        print(f"""
            Количество Ангаров {vehicles_data['fields']['hangars']}
            1) Добавить 1 ангар 
            2) Удалить 1 ангар
            3) Удалить т/с 
            4) Выйти в меню""")
        
        num = int(input("Введите число для взаимодействия "))
        
        if num == 1: 
            with open("transport/database.json", 'r', encoding='utf-8') as file:
                vehicles_data = json.load(file)
                vehicles_data['fields']['hangars'] += 1  #Добавление к ангарам 1
                print("Ангар добавлен.")
                
                with open("transport/database.json", 'w', encoding='utf-8') as outfile:
                    json.dump(vehicles_data, outfile, ensure_ascii=False, indent=4)
                    
        elif num == 2:
            with open("transport/database.json", 'r', encoding='utf-8') as file:
                vehicles_data = json.load(file)
                
                #Нахождение количества т/с в файле
                for a in vehicles_data['fields']['vehicles'] :
                    counter +=1 
                    
                #Проверка если удалить ангар будет ли хватать места на все машины
                if vehicles_data['fields']['hangars'] - 1 >= counter:
                    vehicles_data['fields']['hangars'] -= 1 
                    print("Ангар удален.")
                    
                    with open("transport/database.json", 'w', encoding='utf-8') as outfile:
                        json.dump(vehicles_data, outfile, ensure_ascii=False, indent=4)
                        
                else:
                    print("Невозможно удалить ангар ")

        
        elif num == 3:
            company.list_vehicles()  #Вывод списка т/с компании 
            id_del = str(input("Введите айди т/с "))
            
            with open("transport/database.json", 'r', encoding='utf-8') as file:
                vehicles_data = json.load(file)
                vehicles = vehicles_data['fields']['vehicles']
                
                for vehicle in vehicles:
                    if vehicle['vehicle_id'] == id_del:
                        vehicles.remove(vehicle) #Удаление т/с из файла
                        
                        with open("transport/database.json", 'w', encoding='utf-8') as outfile:
                            json.dump(vehicles_data, outfile, ensure_ascii=False, indent=4)
                            
                        print(f"Т/с с айди {id_del} удалено.")
                        break
                else:
                    print(f"Т/с с айди {id_del} не найдено.")

#Закрытие доп.меню по флажку
        elif num == 4:
            hangar_close = False

#Если ввод не удовлетворяет условиям 
        else:    
            print("От 1 до 4")



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
                hangar()
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

