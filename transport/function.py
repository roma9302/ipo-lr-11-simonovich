#Логика нахождения минимально возможного количества грузовиков т/к
def main(transports): 
    gruz = 7
    counter = 0
    list_ts = []

    def get_ts(vehicle):  #функция для принятия грузоподъемности каждой из машин
        return vehicle['ts']

    
    transports.sort(key=get_ts)  #сортировка (здесь они сортируются в обратном порядке [1,2,3] )
    transports.reverse()  #тут мы переворачиваем сортированый список ([3,2,1])

    for transport in transports: #логика нахождения груза
        if gruz >= transport['ts']:
            while gruz > 0 and transport['ts'] <= gruz:
                gruz -= transport['ts']  
                transport['count'] += 1  #добавление к количеству use грузовиков
                counter += 1  # общий счетчик грузовиков

    if gruz > 0:  #логика нахождения колва авто,если груз меньше ,чем грузоподъемность
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
            print(f"Транспорт с вместимостью {transport['ts']} использован {transport['count']} раз")

    print("Минимально подходящий транспорт для оставшегося груза:", list_ts)


"""t1 = {'ts': 40, 'count': 0}
t2 = {'ts': 2, 'count': 0}
t3 = {'ts': 8, 'count': 0}
t4 = {'ts': 10, 'count': 0}
t5 = {'ts': 8, 'count': 0}
tra = [t1, t2, t3, t4, t5]

main(tra)
"""



#чото другое
