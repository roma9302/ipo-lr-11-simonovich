import json
from .transport_company import TransportCompany

company = TransportCompany("Транспортная компания")


class Hangar:
    def hangar_menu():
        try:
            hangar_close = True #Флажок для выхода из доп. меню
            while hangar_close: 
                
                with open("transport/database.json", 'r', encoding='utf-8') as file:
                    hangar_count = json.load(file)
                counter =0 # подсчет количества т/с в т/к (1 ангар - 1 т/с)
                
                print(f"""
                    Количество Ангаров {hangar_count['fields']['hangars']}
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

        except:
            print("У вас возникла ошибка. Вы возвращены в главное меню.")


