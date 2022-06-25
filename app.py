from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from PIL import Image
from io import BytesIO
import os.path

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

EMAIL = "cristhoffer.santos@jbq.global"
PASSWORD = "AaSsDdFf@135"
URL = "https://portal.azure.com/#@jbq.global/dashboard/arm/subscriptions/5890a983-00c5-45f5-99e1-5fa5d73ac9d2/resourcegroups/qualidoc/providers/microsoft.portal/dashboards/62d73343-baea-4c7c-af07-de002d8be3b5"

def login():
    driver.get(URL)

    driver.implicitly_wait(5)

    email_input = driver.find_element_by_id('i0116')
    email_input.clear()
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.RETURN)

    password_input = driver.find_element_by_id('i0118')
    password_input.send_keys(PASSWORD)

    sleep(3)

    btn_login = driver.find_element_by_id('idSIButton9')
    ActionChains(driver).click(btn_login).perform()

    sleep(3)

    btn_login = driver.find_element_by_id('idSIButton9')
    ActionChains(driver).click(btn_login).perform()

def take_screenshot(browser):
    S = lambda X: browser.execute_script('return document.body.parentNode.scroll'+X)
    browser.set_window_size(S('Width' + 1120,S('Height')) + 2800)
    png = browser.get_screenshot_as_png()

    pedidos = browser.find_element_by_xpath("//*[@id='_weave_e_45']/div[1]/div[2]/div[2]/h3")
    crop(pedidos, "pedido", png)

def crop(element, name, png):
    location = element.location
    size = element.size
    w, h = size['width'], size['height']
    file_name = "img_" + name + ".png"
    handle_print(location, size, file_name, png)

def handle_print(location, size, name, png):

    im = Image.open(BytesIO(png))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom))
    im.save(os.path.dirname(os.path.abspath(__file__)) + "/images/" + name)

def main():
    print("####			Starting		####")
    login()

    sleep(20)
    print("####			Qualidoc		####")
    take_screenshot(driver)