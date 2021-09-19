from datetime import datetime,timedelta
from business_duration import businessDuration
import pandas as pd
from datetime import time,datetime,date
import holidays as pyholidays
import calendar
import locale

class Horas_Laborales:

    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'es_CO')
        self.fmt = "%d/%m/%Y %H:%M:%S"
        fecha1_str = '01/09/2021 00:00:00 + 1100'
        fecha2_str = '30/09/2021 00:00:00 - 1100'
    
        fecha1 = datetime.strptime(fecha1_str[:-7],self.fmt)
        fecha2 = datetime.strptime(fecha2_str[:-7],self.fmt)
        
        print('fecha A = ' + fecha1_str)
        print('fecha B = ' + fecha2_str)

        print('\nRepeticiones por dia entre las fechas' )
        print(self.contador_dias(fecha1, fecha2))

        festivos = pyholidays.Colombia()
        hora_open = time(8,0,0)
        hora_close = time(16,0,0)
        print('\nNo Horas laborales entre las fechas: ' 
             + str(businessDuration(fecha1,fecha2,starttime = hora_open,endtime = hora_close,holidaylist=festivos,unit='hour')))

        print('\nDiferencias entre las fechas asumiendo que estan en la misma zona horaria')
        self.calcularDifFechas(fecha1,fecha2)

        fecha1_utc = self.convertirUTC(fecha1_str)
        fecha2_utc = self.convertirUTC(fecha2_str)
        diff_utc = fecha2_utc - fecha1_utc
        
        print('\nDiferencias entre las fechas tomando en cuenta el offset de las fechas')
        print('Numero de dias Calendario entre las fechas: '+str(diff_utc.days))
        self.calcularDifFechas(fecha1_utc,fecha2_utc)

    def convertirUTC(self,par_fecha):
        fecha = datetime.strptime(par_fecha[:-7],self.fmt)
        timezone= par_fecha[-6:].replace(" ","")
        add = timezone[0]
        hora_offset= int(timezone[0:3])
        min_offset= int(add+timezone[4:6])
        fecha_utc = fecha + timedelta(minutes=min_offset) + timedelta(hours=hora_offset)
        return fecha_utc

    def calcularDifFechas(self,par_fecha1,par_fecha2):
        diff = par_fecha2 - par_fecha1
        print('\tDiferencia en Segundos Calendario: ' + str((diff.days*86400)+diff.seconds))
        print('\tDiferencia en Horas Calendario: ' + str((diff.days*24)+(diff.seconds/3600)))
        print('\tDiferencia en Dias Calendario: ' + str(diff.days))

    def contador_dias(self,par_fecha1, par_fecha2):
        result = {}
        for i in range((par_fecha2 - par_fecha1).days+1):
            dia = calendar.day_name[(par_fecha1 + timedelta(days=i)).weekday()]
            result[dia] = result[dia] + 1 if dia in result else 1
        return result

Horas_Laborales()