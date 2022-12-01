import time
import rrdtool
from getSNMP import consultaSNMP

def update(oids):
    rrdpath = '/home/trophy/PycharmProjects/practicasASR/Practica 3/RRD/'
    carga_CPU = 0
    carga_RAM = 0
    carga_NET = 0

    while 1:
        carga_CPU = int(consultaSNMP('comunidadLuisPersonal','localhost',str(oids[0])))
        carga_RAM = int(consultaSNMP('comunidadLuisPersonal','localhost',str(oids[1])))
        carga_NET = int(consultaSNMP('comunidadLuisPersonal','localhost',str(oids[2])))
        valor = "N:" + str(carga_CPU) + ":" + str(carga_RAM) + ":" + str(carga_NET)
        #print (valor)
        rrdtool.update(rrdpath+'trend.rrd', valor)
       # rrdtool.dump(rrdpath+'trend.rrd','trend.xml')
        time.sleep(5)

    if ret:
        print(rrdtool.error())
        #time.sleep(300)
