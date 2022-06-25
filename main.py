from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")

options.add_argument("start-maximized")

options.add_argument("--disable-extensions")
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs", prefs)

options.headless = True

browser = webdriver.Chrome( options=options)

email = "cristhoffer.santos@jbq.global"
password = "AaSsDdFf@135"
url = "https://portal.azure.com/#@jbq.global/dashboard/arm/subscriptions/5890a983-00c5-45f5-99e1-5fa5d73ac9d2/resourcegroups/qualidoc/providers/microsoft.portal/dashboards/62d73343-baea-4c7c-af07-de002d8be3b5"

browser.get(url)
browser.implicitly_wait(5)