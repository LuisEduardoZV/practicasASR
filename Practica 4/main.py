from telnet import genera_startup_config_file
from ftp import enviar_archivo, obtener_archivo

conection = 1
while conection != 0:
    HOST = input("Ingrese la IP del router a conectar: ")

    user = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña del router: ")
    print("\n*****Al ejecutar el programa se generara el archivo startup-config automaticamente*****")
    genera_startup_config_file(HOST, user, password)

    opcion = 1
    while opcion != 0:
        opcion = int(input("\nIngrese una opcion: \n1)Obtener archivo startup_config\n2)Enviar archivo startup_config\n0)Salir \nR: "))
        
        if opcion == 1:
            savename = input("\nIngrese el nombre de guardado del archivo: ")
            obtener_archivo(HOST, user, password, savename)
        elif opcion == 2:
            filename = input("\nIngrese el nombre del archivo a enviar: ")
            enviar_archivo(HOST, user, password, filename)
        else:
            break
    
    op = int(input("\nDesea cambiar de HOST?\n1)Si\n0)Cerrar programa\nOpcion: "))
    if op == 0:
        conection = 0
    print("\n")