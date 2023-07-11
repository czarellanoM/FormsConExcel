from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


import config
import utils.ApiExcel as ApiExcel
import utils.read_json as read_json

import time


# Extrae los datos de Google Sheets y los guarda en la carpeta de archivos
ApiExcel.fetch_data_from_google_sheets(config.URL_DOCS_EXCLE)

DATOS = read_json.process_data('archivos\datos.json')


# Inicializar el controlador de Chrome
driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)


# Navegar a la página de Microsoft Forms
driver.get(config.URL_FORMS_MICROSOFT)


# Esperar a que la página cargue completamente
# Espera un máximo de 5 segundos para que se cargue la página
driver.implicitly_wait(5)
driver.maximize_window()  # Maximiza el navegador


# Seleciona
def wait_element_to_be_clickable_and_click(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


def wait_presence_of_element_located_and_click_element(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.presence_of_element_located((locator)))
    element.click()


count_successfully = 0
count_wrong_shipments = 0

for dato in DATOS:

    # Seleciona reguional de sur
    select_reguional = (
        By.XPATH, '//*[@id="question-list"]/div[1]/div[2]/div/div/div/span[1]')
    wait_element_to_be_clickable_and_click(driver, select_reguional)

    select_sur = (By.XPATH, '/html/body/div[2]/div/div')
    wait_element_to_be_clickable_and_click(driver, select_sur)

    # Seleciona la tienda de Palmeto
    select_tienda_sur = (
        By.XPATH, '//*[@id="question-list"]/div[2]/div[2]/div/div/div/span[1]')
    wait_element_to_be_clickable_and_click(driver, select_tienda_sur)

    select_tienda_sur_palmeto = (
        By.XPATH, '/html/body/div[2]/div/div[13]/span[2]/span')
    wait_element_to_be_clickable_and_click(driver, select_tienda_sur_palmeto)

    # Seleciona el Tactico a enviar
    if dato['tactico_entregar'] == 'PORTAFREE CON SCORE 38,5K':
        print('PORTAFREE CON SCORE 38,5K')
        select_input_38_5 = (
            By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div/label/span[1]/input')
        wait_presence_of_element_located_and_click_element(
            driver, select_input_38_5)

    elif dato['tactico_entregar'] == 'PORTAFREE CON SOCRE 48,5K':
        print('PORTAFREE CON SOCRE 48,5K')
        select_input_48_5 = (
            By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div/label/span[1]/input')
        wait_presence_of_element_located_and_click_element(
            driver, select_input_48_5)

    else:
        print('ERRROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')

    # Envia el numero de la linea Beneficiaria
    select_Linea_Beneficiario = (
        By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/div/span/input')
    element_Lb = driver.find_element(*select_Linea_Beneficiario)
    element_Lb.send_keys(str(dato['LineaBeneficio']))

    # Envia el numro de la linea Dummie
    select_Dummie = (
        By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[5]/div[2]/div/span/input')
    element_Dmm = driver.find_element(*select_Dummie)
    element_Dmm.send_keys(str(dato['Dummi']))

    # Envia la infomarcion oprimiendo el boton enviar
    BotonSubmit = '/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[3]/div/button'
    element = driver.find_element(By.XPATH, BotonSubmit)
    element.click()

    # Cuenta los envios exitosos y los errados
    try:
        boton = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'Enviar otra respuesta')))
        boton.click()
        print(
            f"Envío exitoso - Línea {dato['LineaBeneficio']}: {dato['Dummi']}")
        driver.implicitly_wait(3)
        count_successfully += 1
        driver.refresh()
    except:
        print(
            f"Error de envío - Línea {dato['LineaBeneficio']}: {dato['Dummi']}")
        driver.implicitly_wait(3)
        count_wrong_shipments += 1
        driver.refresh()

# Imprime el numero de envios exitosos y fallidos
print(f'Se enviaron Exitosamente {count_successfully} datos')
print(f'Numero de envíos errados {count_wrong_shipments}')
