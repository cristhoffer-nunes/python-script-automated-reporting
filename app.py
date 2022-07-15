from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, glob 

import painel_infos
import create_report
import send_email


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")

options.add_argument("start-maximized")

options.add_argument("--disable-extensions")
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs", prefs)

options.headless = True

def delete_arqs():
    for filename in glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/images/img*"):
        if os.path.isfile(filename):
            os.remove(filename)

    if os.path.isfile("Relatório.pdf"):
        os.remove("Relatório.pdf")

# CREDENCIAIS PARA ACESSO AO PAINEL PARA SCREENSHOT (NAO SUBSTITUIR AS CREDENCIAIS)
EMAIL = "cristhoffer.santos@jbq.global"
PASSWORD = "AaSsDdFf@135"
URL = "https://portal.azure.com/#@jbq.global/dashboard/private/b45f67ab-aa45-4b80-bfb9-014009bfe23e"

def login():
    driver.get(URL)

    driver.implicitly_wait(5)
    email_input = driver.find_element(By.ID,"i0116")
    email_input.clear()
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.RETURN)

    password_input = driver.find_element(By.ID,"i0118")
    password_input.send_keys(PASSWORD)

    sleep(3)

    btn_login = driver.find_element(By.ID,"idSIButton9")
    ActionChains(driver).click(btn_login).perform()

    sleep(3)

    btn_login = driver.find_element(By.ID,"idSIButton9")
    ActionChains(driver).click(btn_login).perform()

def main():
    print("####			Starting		####")
    login()

    print("####			Screenshot		####") 
    sleep(60) 
    painel_infos.element_capture(driver)

    print("####			Report		####") 
    create_report.report()

    print("####			Send email		####") 
    send_email.send_email()

    print("####			EXIT		####") 
    
    delete_arqs()
    driver.quit()
    