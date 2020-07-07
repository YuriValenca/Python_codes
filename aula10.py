from datetime import date, time, datetime, timedelta

def trab_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    tupla = ('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20) #formato: ano, mes, dia, hora, min, sec
    print(data_criada)
    print(data_criada.strftime('%c'))

def trab_timedelta():
    data_atual = datetime.now()
    nova_data = data_atual - timedelta(days=365)
    print(nova_data.strftime('%c'))


def trab_data():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %Y'))

def trab_time():
    horario = time(hour = 15, minute = 20, second = 30)
    print(horario.strftime('%H:%M:%S'))
    #OU
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

if __name__ == '__main__':
    # trab_data()
    # # trab_time()
    # trab_datetime()
    trab_timedelta()