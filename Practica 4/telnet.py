import telnetlib

def genera_startup_config_file(HOST, user, password):

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"User: ")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    tn.write(b"en\n")
    tn.write(b"conf\n")
    tn.write(b"service ftp\n")
    tn.write(b"copy run start\n")
    tn.write(b"exit\n")
    tn.write(b"exit\n")
    #print(tn.read_all().decode('utf-8'))
    return 1
