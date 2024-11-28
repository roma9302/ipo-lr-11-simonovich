#Логика нахождения минимально возможного количества грузовиков т/к
def main(transports):
    gruz = 42
    counter = 0
    list_ts = []

    def get_ts(vehicle):
        return vehicle['ts']

    
    transports.sort(key=get_ts)
    transports.reverse()

    for transport in transports:
        if gruz >= transport['ts']:
            while gruz > 0 and transport['ts'] <= gruz:
                gruz -= transport['ts']  
                transport['count'] += 1  
                counter += 1  
                
    if gruz > 0:  
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

main(tra)
"""


# чото другое
