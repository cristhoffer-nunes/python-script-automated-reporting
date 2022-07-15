import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

dateTimeObj = datetime.now()
ano = dateTimeObj.year
mes = dateTimeObj.month
dia = dateTimeObj.day

EMAIL = "cristhoffer.santos@jbq.global"
PASSWD = "AaSsDdFf@135"


contatos = ['xotakuxpower@gmail.com']

def send_email():
    msg = EmailMessage()
    msg['Subject'] = f'Relatório Diário - TrendFoods - {dia}/{mes}/{ano}'
    msg['From'] = EMAIL
    msg['To'] = ', '.join(contatos)
    msg.set_content('Boa noite, prezados. Segue em anexo o PDF com o relatório diário TrendFoods')

    with open('Relatório.pdf', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL, PASSWD)
        smtp.send_message(msg)

        f = open(os.path.dirname(os.path.abspath(__file__)) + "/last _report_day.txt", "w")
        f.write(str(dia))
