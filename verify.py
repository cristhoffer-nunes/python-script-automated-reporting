import os
from datetime import datetime
x = datetime.now()
hoje = x.day
mes = x.month
ano = x.year

def dayReport(day):
    day = int(day)
    if(int(hoje) - day > 1 or int(hoje) - day < 0):
        import app
        app.main()
    else:
        print(f'#### Relatório já foi encaminhado em {hoje}/{mes}/{ano} ####')


def existReportTxt():

    if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/last _report_day.txt"):
        with open(os.path.dirname(os.path.abspath(__file__)) + "/last _report_day.txt") as f:
            dia = f.readline()

            dayReport(dia)
  
    else:
        print('Arquivo TXT não existe')

existReportTxt()