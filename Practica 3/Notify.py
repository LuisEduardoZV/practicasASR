import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', '
# Define params
rrdpath = '/home/trophy/PycharmProjects/practicasASR/Practica 3/RRD/'
imgpath = '/home/trophy/PycharmProjects/practicasASR/Practica 3/IMG/'
fname = 'trend.rrd'

mailsender = "lezv.dc@gmail.com"
mailreceip = "lezv.dc@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'vdrhtrfhflhmjqll'

def send_alert_attached(subject, data):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(imgpath+'deteccion.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    msg.attach(MIMEText(str(data[0]+"\n"),'plain'))
    msg.attach(MIMEText(str(data[1]+"\n"),'plain'))
    msg.attach(MIMEText(str(data[2]+"\n"),'plain'))
    msg.attach(MIMEText(str(data[3]+"\n"),'plain'))
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()