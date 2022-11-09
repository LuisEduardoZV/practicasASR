import time
import rrdtool
from getSNMP import consultaSNMP

def updateRRD(oids):
    while 1:
        unicast = int(
            consultaSNMP('comunidadLuisPersonal','localhost',
                         str(oids[0])))
        paquetes = int(
            consultaSNMP('comunidadLuisPersonal','localhost',
                         str(oids[1])))
        icmp = int(
            consultaSNMP('comunidadLuisPersonal','localhost',
                         str(oids[2])))
        segmentos = int(
            consultaSNMP('comunidadLuisPersonal','localhost',
                         str(oids[3])))
        datagramas = int(
            consultaSNMP('comunidadLuisPersonal','localhost',
                         str(oids[4])))

        valor = "N:" + str(unicast) + ':' + str(paquetes) + ':' + str(icmp) + ':' + str(segmentos) + ':' + str(datagramas)
        #print (valor)
        rrdtool.update('practicaRRD.rrd', valor)
        time.sleep(1)
