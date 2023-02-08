import time
import datetime
from typing import Text

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from function import *

browser = webdriver.Chrome()

#definicion del link a testear
browser.get(link1)

browser.maximize_window()

title = browser.title
##assert title == 'Mercado Libre'

browser.implicitly_wait(20)
buscar_selenium = browser.find_element(by=By.NAME, value="as_word")
presionar_busqueda = browser.find_element(by=By.CLASS_NAME, value="nav-search-btn")

buscar_selenium.send_keys('pantalon hombre')
presionar_busqueda.click()

buscar_selenium = browser.find_element(by=By.NAME, value="as_word")
valor = buscar_selenium.get_attribute('value')
assert valor == "pantalon hombre"

usado =browser.find_element(By.XPATH,"//span[contains(.,'Usado')]")
#aqui buscar el nombre de ACEPTAR de la cookie
#presionar_cookie = browser.find_element(by=By.CLASS_NAME, value="cookie-consent-banner-opt-out__action cookie-consent-banner-opt-out__action--primary cookie-consent-banner-opt-out__action--key-accept")
#presionar_cookie = browser.find_element(by=By.ID,value="action:understood-button")
# dar click en aceptar cookie
#presionar_cookie.click()
#time.sleep(10)

usado.click()
time.sleep(1000)
browser.quit()
