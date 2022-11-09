import rrdtool

def createRRD():
    ret = rrdtool.create("practicaRRD.rrd",
                         "--start",'N',
                         "--step",'100',
                         "DS:unicast:COUNTER:120:U:U",
                         "DS:paquetes:COUNTER:120:U:U",
                         "DS:icmp:COUNTER:120:U:U",
                         "DS:segmentos:COUNTER:120:U:U",
                         "DS:datagramas:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:5:1500",
                         "RRA:AVERAGE:0.5:5:1500",
                         "RRA:AVERAGE:0.5:5:1500",
                         "RRA:AVERAGE:0.5:5:1500",
                         "RRA:AVERAGE:0.5:5:1500")
    return ret