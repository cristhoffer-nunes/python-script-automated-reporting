from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import time
import csv
import prettytable

LOGS_URL = f"https://portal.azure.com/#blade/Microsoft_Azure_Monitoring_Logs/LogsBlade/scope/%7B%22resources%22%3A%5B%7B%22resourceId%22%3A%22%2Fsubscriptions%2F5890a983-00c5-45f5-99e1-5fa5d73ac9d2%2Fresourcegroups%2Ftrendfoods%2Fproviders%2Fmicrosoft.operationalinsights%2Fworkspaces%2Ftrendworkspaceloganalytics%22%7D%5D%7D/source/LogAnalyticsExtension.GoToLogsBladeCommand/query/mt_ContainerLogStat%0A%7C%20where%20NameBase%20contains%20%22PRD%22%0A%7C%20extend%20RateError%20%3D%20RateError*100%0A%7C%20sort%20by%20RateError%20desc%0A%7C%20project%20Nome%20%3D%20NameBase%2C%20TaxaErro%20%3D%20RateError%2C%20Info%20%3D%20Info%2C%20Alert%20%3D%20Warn%2C%20Err%20%3D%20Error%0A%7C%20render%20table%20with%20(title%3D%22Aplica%C3%A7%C3%B5es%20logs%22)/prettify/1/timespan/PT24H"

def get_logs(browser):
    logs=0
    browser.get(LOGS_URL)
    browser.refresh()
    
    time.sleep(15)
    iframe = browser.find_element(By.XPATH,"(//iframe)[1]")
    browser.switch_to.frame(iframe)

    try:
        browser.implicitly_wait(30)
        element = browser.find_element(By.XPATH,"//span//span")
        if(element.text == '50'):
            logs = 1
    finally:
        print("Finally")

    if logs == 1:
        count = 0
        span = browser.find_element(By.XPATH,"//span//span[text() = '50']")
        span.click()
        qtd_res = browser.find_element(By.XPATH,"//li[text() = '200']")
        qtd_res.click()

        rows = browser.find_element(By.XPATH,"//tr[contains(@class, 'k-master-row')]")
        
        f = open("app_logs.csv", "w")
        f.write("Nome,TaxaErro,Info,Alert,Err")
        f.write("\n")
        for x in range(len(rows)):
            content = browser.find_element(By.XPATH,f"//tr[contains(@class, 'k-master-row')][{x+1}]//td")
            taxaErro = browser.find_element(By.XPATH,f"//tr[contains(@class, 'k-master-row')][{x+1}]//td[3]").text
            taxaErro = taxaErro.replace(',','.')
            if float(taxaErro) < 5.0:
                continue
            for y in range(2, len(content)):
                count += 1
                value = browser.find_element(By.XPATH,f"//tr[contains(@class, 'k-master-row')][{x+1}]//td[{y}]")
                test = value.text.replace(',','.')
                f.write(test)
                if y < 6:
                    f.write(",")
            if x < len(rows):
                f.write("\n")
        f.close()
        if count == 0:
            f = open("app_logs.csv", "w")
            f.write("Nenhuma taxa de erro superior a 5%")
            f.close()
    browser.switch_to_default_content()

def get_data_from_prettytable(data):
    def remove_space(liste):
        list_without_space = []
        for mot in liste:                                
            word_without_space = mot.replace(' ', '')    
            list_without_space.append(word_without_space)
        return list_without_space

    string_x = str(data).split('\n')                               
    header = string_x[1].split('|')[1: -1]                      
    rows = string_x[3:len(string_x) - 1]                        

    list_word_per_row = []
    for row in rows:                                            
        row_resize = row.split('|')[1:-1]                       
        list_word_per_row.append(remove_space(row_resize))      

    return header, list_word_per_row


def create_log_table(header, data, pdf):

    pdf.set_font("Arial", size=10)             
    epw = pdf.w - 2*pdf.l_margin               
    col_width = pdf.w / 4.5                    
    row_height = pdf.font_size * 1.5           
    spacing = 1.3                         
 
    pdf.ln(row_height*spacing)                 


    for item in header:                        
        if "Nome" in item: largura = col_width + 62
        else: largura = col_width - 28
        pdf.cell(largura, row_height*spacing,
                txt=item, border=1)
    pdf.ln(row_height*spacing)                 

    for row in data:                           
        for item in row:
            if item.startswith("PRD"): largura = col_width + 62
            else: largura = col_width - 28
            pdf.cell(largura, row_height*spacing,
                    txt=item, border=1)
        pdf.ln(row_height*spacing)

def create_logs(pdf):
    pdf = pdf
    if(os.path.isfile("app_logs.csv")):
        with open('app_logs.csv') as f:
            first_line = f.readline()

        if(first_line == "Nenhuma taxa de erro superior a 5%"):
            pdf.set_font('Arial', '', 14)
            pdf.ln(15)
            pdf.write(5, f'Nenhuma taxa de erro superior a 5%')
        else:
            reader = csv.reader(open("app_logs.csv", "r"))
            data = []
            for row in reader:
                data.append(row)

            header = data.pop(0)
            table = prettytable.PrettyTable(header)

            for row in (data):
                table.add_row(row)

            h,d = get_data_from_prettytable(table)
            create_log_table(h,d, pdf)
    else:
        pdf.set_font('Arial', '', 14)
        pdf.write(5, f'Tempo máximo de espera excedido')