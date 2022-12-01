import sys
import rrdtool
from  Notify import send_alert_attached
import time
rrdpath = '/home/trophy/PycharmProjects/practicasASR/Practica 3/RRD/'
imgpath = '/home/trophy/PycharmProjects/practicasASR/Practica 3/IMG/'

def generarGraficaCPU(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 900
    ret = rrdtool.graphv( imgpath+"deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Cpu load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Carga del CPU \nUsando SNMP y RRDtools \n Detección de umbrales",
                    "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                     "CDEF:umbral25=cargaCPU,25,LT,0,cargaCPU,IF",
                     "CDEF:umbral50=cargaCPU,50,LT,0,cargaCPU,IF",
                     "CDEF:umbral90=cargaCPU,90,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#3b83bd:Carga del CPU",
                     "AREA:umbral25#008000:Carga CPU mayor de 25",
                     "AREA:umbral50#FF9F00:Carga CPU mayor de 50",
                     "AREA:umbral90#FF0000:Carga CPU mayor de 90",
                     "HRULE:25#008000:Umbral  25%",
                     "HRULE:50#FF9F00:Umbral  50%",
                     "HRULE:90#FF0000:Umbral  90%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )

def generarGraficaRAM(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv( imgpath+"deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=RAM load",
                    '--lower-limit', '0',
                    "--title=Carga de RAM \nUsando SNMP y RRDtools \n Detección de umbrales",
                    "DEF:cargaRAM="+rrdpath+"trend.rrd:RAMload:AVERAGE",
                     "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                     "VDEF:cargaMIN=cargaRAM,MINIMUM",
                     "VDEF:cargaSTDEV=cargaRAM,STDEV",
                     "VDEF:cargaLAST=cargaRAM,LAST",
                     #"CDEF:umbral50=cargaRAM,50,LT,0,cargaRAM,IF",
                     "AREA:cargaRAM#00FF00:Carga de la RAM",
                     #"AREA:umbral50#FF9F00:Carga CPU mayor de 50",
                     #"HRULE:50#FF0000:Umbral  50%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )

def generarGraficaNET(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv( imgpath+"deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=RAM load",
                    '--lower-limit', '0',
                    "--title=Carga de RAM \nUsando SNMP y RRDtools \n Detección de umbrales",
                    "DEF:cargaRAM="+rrdpath+"trend.rrd:RAMload:AVERAGE",
                     "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                     "VDEF:cargaMIN=cargaRAM,MINIMUM",
                     "VDEF:cargaSTDEV=cargaRAM,STDEV",
                     "VDEF:cargaLAST=cargaRAM,LAST",
                     #"CDEF:umbral50=cargaRAM,50,LT,0,cargaRAM,IF",
                     "AREA:cargaRAM#00FF00:Carga de la RAM",
                     #"AREA:umbral50#FF9F00:Carga CPU mayor de 50",
                     #"HRULE:50#FF0000:Umbral  50%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )

def monitoreo(tipo, data):
    while (1):
        ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trend.rrd")
        timestamp = ultima_actualizacion['date'].timestamp()
        carga_CPU = ultima_actualizacion['ds']["CPUload"]
        carga_RAM = ultima_actualizacion['ds']["RAMload"]
        carga_NET = ultima_actualizacion['ds']["NETload"]
        #print(carga_CPU, carga_RAM, carga_NET)
        print("Monitoreando...")
        if tipo == 1:
            if carga_CPU >= 25 and carga_CPU < 50:
                generarGraficaCPU(int(timestamp))
                send_alert_attached("Sobrepasa el umbral 25% - Luis Z", data)
                print("sobrepasa el umbral 25%")
            elif carga_CPU >= 50 and carga_CPU < 85:
                generarGraficaCPU(int(timestamp))
                send_alert_attached("Sobrepasa el umbral 50% - Luis Z", data)
                print("sobrepasa el umbral 50%")
            elif carga_CPU >= 90:
                generarGraficaCPU(int(timestamp))
                send_alert_attached("Sobrepasa el umbral 90% - Luis Z", data)
                print("sobrepasa el umbral 90%")
        elif tipo == 2:
            if carga_RAM >= 25:
                generarGraficaRAM(int(timestamp))
                send_alert_attached("Sobrepasa el umbral")
                print("sobrepasa el umbral")
            elif carga_RAM >= 50:
                generarGraficaRAM(int(timestamp))
                send_alert_attached("Sobrepasa el umbral")
                print("sobrepasa el umbral")
            elif carga_RAM >= 90:
                generarGraficaRAM(int(timestamp))
                send_alert_attached("Sobrepasa el umbral")
                print("sobrepasa el umbral")
        elif tipo == 3:
            if carga_NET >= 25:
                generarGraficaNET(int(timestamp))
                send_alert_attached("Sobrepasa el umbral")
                print("sobrepasa el umbral")
            elif carga_NET >= 50:
                generarGraficaNET(int(timestamp))
                send_alert_attached("Sobrepasa el umbral")
                print("sobrepasa el umbral")
            elif carga_NET >= 90:
                generarGraficaNET(int(timestamp))
                send_alert_attached("Sobrepasa el umbral")
                print("sobrepasa el umbral")
        time.sleep(1)