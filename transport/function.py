#Логика нахождения минимально возможного количества грузовиков т/к
def main(transports,gru):
    gruz = gru
    counter = 0
    list_ts = []

    def get_ts(vehicle): #функция получения т/с
        return vehicle['ts']

    
    transports.sort(key=get_ts) #сортировка транспорта в порядке возврастания 
    transports.reverse()  #реверс сортированного списка в порядке возврастания

    for transport in transports: # логика нахождения оптимального количества т/с
        if gruz >= transport['ts']:
            while gruz > 0 and transport['ts'] <= gruz:
                gruz -= transport['ts']  
                transport['count'] += 1  
                counter += 1  
                
    if gruz > 0:   # логика ,если груз меньше ,чем  грузоподьемность любой из т/с
        is_have = None
        for transport in transports: 
            if transport['ts'] > gruz:
                if is_have is None or transport['ts'] < is_have['ts']:
                    is_have = transport
        if is_have:
            list_ts.append(is_have['ts'])

    
    print("Количество использованного транспорта:", counter)
    for transport in transports:
        if transport['count'] > 0:
            print(f"Транспорт с вместимостью {transport['ts']} использован {transport['count']} раз(а) тип транспорта {transport['type']}")

    print("Минимально подходящий транспорт для оставшегося груза:", list_ts)

"""
t1 = {'ts': 40, 'count': 0 , 'type': 'airplane' }
t2 = {'ts': 2, 'count': 0, 'type' :'van' }
t3 = {'ts': 8, 'count': 0,'type': 'van' }
t4 = {'ts': 10, 'count': 0 ,' type ' :'airplane'}
t5 = {'ts': 8, 'count': 0 ,' type' : 'van '}
tra = [t1, t2, t3, t4, t5]

main(tra,42)
"""



# чото другое
