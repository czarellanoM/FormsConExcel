from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


import config


import time


# Inicializar el controlador de Chrome
driver = webdriver.Chrome(executable_path='chromedriver\chromedriver.exe')


# Navegar a la página de Microsoft Forms
driver.get('www.google.com')

time.sleep(100)
driver.quit()
