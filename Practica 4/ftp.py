from ftplib import FTP

def obtener_archivo(host, user, passwd, savename):
    ftp = FTP(host)
    ftp.login(user, passwd)
    with open(savename, 'wb') as fp:
        ftp.retrbinary('RETR startup-config', fp.write)
    ftp.quit()
    print("\n*******Archivo obtenido*******\n")
    return 1

def enviar_archivo(host, user, passwd, filename):
    ftp = FTP(host)
    ftp.login(user, passwd)
    with open(filename, 'rb') as fp:
        ftp.storbinary('STOR startup-config', fp)
    ftp.quit()
    print("\n*******Archivo enviado*******\n")
    return 1