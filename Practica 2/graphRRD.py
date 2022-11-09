import sys
import rrdtool
import time

def createGraph():
  tiempo_actual = int(time.time())
  tiempo_inicial = tiempo_actual - 350
  rrdtool.graphv("unicast.png",
                  "--start",str(tiempo_inicial),
                  "--end","N",
                  "--vertical-label=Paquetes Unicast",
                  "--title=Paquetes unicast recibidos \n Usando SNMP y RRDtools",
                  "DEF:sEntrada=practicaRRD.rrd:unicast:AVERAGE",
                  "VDEF:segEntradaLast=sEntrada,LAST",
                  "VDEF:segEntradaFirst=sEntrada,FIRST",
                  "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                  "PRINT:segEntradaLast:%6.2lf",
                  "PRINT:segEntradaFirst:%6.2lf",
                  "GPRINT:segEntradaMax:%6.2lf %S paqEntMAX",
                  "AREA:sEntrada#FF0000:Paquetes unicast")
  rrdtool.graphv("paquetes.png",
                  "--start",str(tiempo_inicial),
                  "--end","N",
                  "--vertical-label=Paquetes recibidos a IPV4",
                  "--title=Paquetes recibidos a IPV4 con errores \n Usando SNMP y RRDtools",
                  "DEF:sEntrada=practicaRRD.rrd:paquetes:AVERAGE",
                  "VDEF:segEntradaLast=sEntrada,LAST",
                  "VDEF:segEntradaFirst=sEntrada,FIRST",
                  "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                  "PRINT:segEntradaLast:%6.2lf",
                  "PRINT:segEntradaFirst:%6.2lf",
                  "GPRINT:segEntradaMax:%6.2lf %S paqEntMAX",
                  "AREA:sEntrada#FF0000:Paquetes IPV4")
  rrdtool.graphv("icmp.png",
                  "--start",str(tiempo_inicial),
                  "--end","N",
                  "--vertical-label=Mensajes ICMP",
                  "--title=Mensajes ICMP echo enviados \n Usando SNMP y RRDtools",
                  "DEF:sEntrada=practicaRRD.rrd:icmp:AVERAGE",
                  "VDEF:segEntradaLast=sEntrada,LAST",
                  "VDEF:segEntradaFirst=sEntrada,FIRST",
                  "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                  "PRINT:segEntradaLast:%6.2lf",
                  "PRINT:segEntradaFirst:%6.2lf",
                  "GPRINT:segEntradaMax:%6.2lf %S msgEntMAX",
                  "AREA:sEntrada#FF0000:Mensajes echo enviados")
  rrdtool.graphv("segmentos.png",
                  "--start",str(tiempo_inicial),
                  "--end","N",
                  "--vertical-label=Segmentos recibidos",
                  "--title=Segmentos recibidos con errores \n Usando SNMP y RRDtools",
                  "DEF:sEntrada=practicaRRD.rrd:segmentos:AVERAGE",
                  "VDEF:segEntradaLast=sEntrada,LAST",
                  "VDEF:segEntradaFirst=sEntrada,FIRST",
                  "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                  "PRINT:segEntradaLast:%6.2lf",
                  "PRINT:segEntradaFirst:%6.2lf",
                  "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                  "AREA:sEntrada#FF0000:Segmentos recibidos")
  rrdtool.graphv("datagramas.png",
                  "--start",str(tiempo_inicial),
                  "--end","N",
                  "--vertical-label=Datagramas enviados",
                  "--title=Datagramas entregados a usuarios UDP \n Usando SNMP y RRDtools",
                  "DEF:sEntrada=practicaRRD.rrd:datagramas:AVERAGE",
                  "VDEF:segEntradaLast=sEntrada,LAST",
                  "VDEF:segEntradaFirst=sEntrada,FIRST",
                  "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                  "PRINT:segEntradaLast:%6.2lf",
                  "PRINT:segEntradaFirst:%6.2lf",
                  "GPRINT:segEntradaMax:%6.2lf %S datEntMAX",
                  "AREA:sEntrada#FF0000:Datagramas entregados")