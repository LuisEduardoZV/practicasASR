# This is a sample Python script.

from pysnmp.hlapi import *
import json

from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from datetime import datetime


def consulta_snmp(comunidad, host, version, puerto, oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad, mpModel=version),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))
    res = ""
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            res = (' = '.join([x.prettyPrint() for x in varBind]))
    return res


def busca_dispositivo(data, type):
    while True:
        nombre = input("Ingrese el nombre del dispositivo: ")
        index = -1
        dato = {}
        for dispositivo in data:
            if dispositivo["Nombre"] == nombre:
                index = data.index(dispositivo)
                dato = dispositivo
                break
        if index != -1:
            break
        else:
            print("El nombre ingresado no se encontro")
    if type == 1:
        return index
    else:
        return index, dato


def agregar(data):
    print("\nAGREGAR")
    print("Introduzca la informacion necesario")
    nombre = input("Nombre del dispositivo: ")
    ip = input("IP: ")
    version = input("Version SNMP: ")
    comunidad = input("Comunidad: ")
    puerto = input("Puerto: ")
    ingreso = {
        "Nombre": nombre,
        "IP": ip,
        "Version": version,
        "Comunidad": comunidad,
        "Puerto": puerto
    }
    data.append(ingreso)
    return data


def actualizar(data):
    print("\nACTUALIZAR")
    index, dato = busca_dispositivo(data, 0)
    del data[index]
    keys = ["Nombre", "IP", "Version", "Comunidad", "Puerto"]
    print(dato)
    for key in keys:
        cambio = input(f"Nuevo {key}(En caso de no querer cambiarlo, introduzca Enter): ")
        if cambio != "":
            dato[key] = cambio
    data.append(dato)
    return data


def eliminar(data):
    print("\nELIMINAR")
    index = busca_dispositivo(data, 1)
    del data[index]
    return data


def obten_data(oids, table, dispositivo):
    res = []
    res_table = []
    index = 1
    version = 0
    if dispositivo["Version"] == "2" or dispositivo["Version"] == "2c":
        version = 1
    puerto = int(dispositivo["Puerto"])
    for oid in oids:
        data = consulta_snmp(dispositivo["Comunidad"], dispositivo["IP"], version, puerto, oid).split()
        if index == 1:
            cadena = " ".join(data[2:])
            position = cadena.find("Software:")
            if position != -1:
                res.append(cadena[position+10:])
            else:
                res.append(data[2] + " " + data[4])
        elif index == 2 or index == 3 or index == 5:
            res.append(data[2])
        elif index == 4:
            res.append(" ".join(data[2:]))
        index = index+1
    #print(res)
    interfaces = int(res[4])
    if interfaces >= 6:
        interfaces = 6
    index = 1
    index_column = 1
    while index <= interfaces:
        row = []
        for column in table:
            oid = column + "" + str(index)
            data = consulta_snmp(dispositivo["Comunidad"], dispositivo["IP"], version, puerto, oid).split()[2]
            if index_column == 2:
                if int(data) == 1:
                    row.append("up")
                elif int(data) == 2:
                    row.append("down")
                elif int(data) == 3:
                    row.append("testing")
            else:
                row.append(data)
            index_column = index_column + 1
        res_table.append(row)
        index = index + 1
        index_column = 1
    #print(res_table)
    return res, res_table


def creaPDF(res, res_table, dispositivo):
    w, h = A4
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y_%H:%M:%S")
    titulo = "Reporte_" + dispositivo['Nombre'] + date_time + ".pdf"
    doc = canvas.Canvas(titulo, pagesize=A4)
    titulos = doc.beginText(30, h-50)
    titulos.setFont("Times-Roman", 18)
    titulos.textLine("Administración de Servicios en Red")
    titulos.textLine("Practica 1")
    titulos.textLine("Luis Eduardo Zúñiga Vera                                                 4CM13")
    doc.drawText(titulos)
    doc.line(10, h-120, w-10, h-120)
    data = doc.beginText(30, h-140)
    data.setFont("Times-Roman", 12)
    data.textLine(f"Sistema y versión: {res[0]}")
    data.textLine(f"Nombre del dispositivo (sistema): {res[1]}")
    data.textLine(f"Nombre del dispositivo (ingresado): {dispositivo['Nombre']}")
    data.textLine(f"IP: {dispositivo['IP']}")
    data.textLine(f"Información de contacto: {res[2]}")
    data.textLine(f"Ubicación: {res[3]}")
    data.textLine(f"Número de interfaces: {res[4]}")
    doc.drawText(data)
    if res[0].lower().find("linux") != -1:
        doc.drawImage('/home/trophy/PycharmProjects/practicasASR/Practica 1/img/linux.jpg', (w/2)+120, (h/2)+180, 100, 100)
    elif res[0].lower().find("windows") != -1:
        doc.drawImage('/home/trophy/PycharmProjects/practicasASR/Practica 1/img/windows.jpg', (w/2)+120, (h/2)+180, 100, 100)
    else:
        doc.drawImage('/home/trophy/PycharmProjects/practicasASR/Practica 1/img/not_found.jpg', (w/2)+120, (h/2)+180, 100, 100)
    content_table = [["Interfaz", "Estado"]]
    for row in res_table:
        content_table.append([row[0], row[1]])
    table_pdf = Table(content_table)
    style = []
    style.append(('GRID', (0, 0), (-1, -1), 0.5, colors.black))
    for row, values in enumerate(content_table):
        style.append(('BACKGROUND', (1, row), (1, row), colors.gray))
    table_pdf.setStyle(TableStyle(style))
    table_pdf.wrapOn(doc, w-10, h-10)
    table_pdf.drawOn(doc, 30, h/2+(160-(17*len(content_table))))
    doc.showPage()
    doc.save()
    return 1


def menu():
    opcion = input("Elige una opcion\n1) Agregar dispositivo\n2) Cambiar informaciòn de dispositivo\n3) Eliminar dispositivo\n"
          "4) Generar reporte\n0) Salir\nOpcion: ")
    opcion = int(opcion)
    return opcion


def abrir_archivo(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def escribir_datos(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


filename = '/home/trophy/PycharmProjects/practicasASR/Practica 1/dispositivos.json'
print("SISTEMA DE ADMINISTRACION DE RED")
print("Practica 1 - Adquisicion de Informacion")
print("Zuniga Vera Luis Eduardo \t 4CM13 \t 2019630093\n")
while True:
    op = menu()
    data = abrir_archivo(filename)

    if op == 1:
        data = agregar(data)
        escribir_datos(data, filename)
        print("\nEl dispositivo se agrego correctamente!!!\n")
    elif op == 2:
        data = actualizar(data)
        escribir_datos(data, filename)
        print("\nEl dispositivo se actualizo correctamente!!!\n")
    elif op == 3:
        data = eliminar(data)
        escribir_datos(data, filename)
        print("\nEl dispositivo se elimino correctamente!!!\n")
    elif op == 4:
        data = abrir_archivo(filename)
        oids = ["1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.5.0", "1.3.6.1.2.1.1.4.0", "1.3.6.1.2.1.1.6.0", "1.3.6.1.2.1.2.1.0"]
        table = ["1.3.6.1.2.1.2.2.1.2.", "1.3.6.1.2.1.2.2.1.7."]
        index = busca_dispositivo(data, 1)
        dispositivo = data[index]
        res, res_table = obten_data(oids, table, dispositivo)
        creaPDF(res, res_table, dispositivo)
        print("\nPDF generado, salga del programa para poder visualizarlo...\n")
    elif op == 0:
        print("Saliendo...")
        break
