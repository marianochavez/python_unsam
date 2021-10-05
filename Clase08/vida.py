from datetime import datetime, timedelta


def vida_en_segundos(fecha_nac):
    """Devuelve la cantidad en segundos desde esa fecha hasta ahora"""
    date_object = datetime.strptime(fecha_nac, '%d/%m/%Y')
    date_now = datetime.now()
    seconds = float((date_now-date_object).total_seconds())
    return seconds


def cuanto_falta(fecha):
    """"Retorna cuantos dias faltan para esa fecha a partir de ahora"""
    date_now = datetime.now()
    date_next = datetime.strptime(fecha, '%d/%m/%Y')
    days = (date_next-date_now).days
    return days


def dias_habiles(inicio, fin, feriados):
    """Devuelve una lista con los dias hábiles, desde inicio hasta fin
        sin incluir los feriados"""

    inicio = datetime.strptime(inicio, '%d/%m/%Y').date()
    fin = datetime.strptime(fin, '%d/%m/%Y').date()
    feriados = [datetime.strptime(feriado, '%d/%m/%Y').date()for feriado in feriados]
    cant_dias = (fin-inicio).days + 1

    dias_laborales = []
    for fecha in [d for d in (inicio + timedelta(n) for n in range(cant_dias)) if d <= fin]:
        if fecha.weekday() < 5:
            if fecha not in [feriado for feriado in feriados]:
                dias_laborales.append(datetime.strftime(fecha, '%d/%m/%Y'))

    return dias_laborales


# print(vida_en_segundos('23/06/1997'))
# print(cuanto_falta('22/12/2021'))
# feriados = ['12/10/2020', '23/11/2020','07/12/2020', '08/12/2020', '25/12/2020']
# print(dias_habiles('20/09/2020', '31/12/2020', feriados))
