import rrdtool
ret = rrdtool.create("/home/trophy/PycharmProjects/practicasASR/Practica 3/RRD/trend.rrd",
                     "--start",'N',
                     "--step",'15',
                     "DS:CPUload:GAUGE:60:0:100",
                     "DS:RAMload:GAUGE:60:U:U",
                     "DS:NETload:GAUGE:60:U:U",
                     "RRA:AVERAGE:0.5:1:24",
                     "RRA:AVERAGE:0.5:1:24",
                     "RRA:AVERAGE:0.5:1:24")
if ret:
    print (rrdtool.error())
