from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controladorintranetPersonal = webdriver.Chrome()
controladorintranetPersonal.get("https://intranet.personalsoft.com/")

#elemento por identificador
'''
usuario = controladorintranetPersonal.find_element(By.ID, "modlgn-username")
usuario.send_keys("catobon")

password = controladorintranetPersonal.find_element(By.ID, "modlgn-passwd")
password.send_keys("Indacoalla1988*/")

botonIngreso = controladorintranetPersonal.find_element(By.NAME,"Submit")
botonIngreso.click()

time.sleep(5)
controladorintranetPersonal.quit()
'''
#xpath ruta relativa
'''
usuario = controladorintranetPersonal.find_element(By.XPATH, "//input[@id='modlgn-username']")
usuario.send_keys("catobon")

password = controladorintranetPersonal.find_element(By.XPATH, "//input[@id='modlgn-passwd']")
password.send_keys("Indacoalla1988*/")

botonIngreso = controladorintranetPersonal.find_element(By.XPATH,"//button[normalize-space()='Identificarse']")
botonIngreso.click()

time.sleep(5)
controladorintranetPersonal.quit()
'''
#xpath ruta absoluta
'''
usuario = controladorintranetPersonal.find_element(By.XPATH, "/html/body/div[@id='g-page-surround']/header[@id='g-header']/div[@class='g-container']/div[@class='g-grid']/div[@id='header']/div[@class='g-content']/div[@class='platform-content']/div[@class='moduletable Form_Home']/form[@id='login-form']/div[@class='userdata']/div[@id='form-login-username']/div[@class='controls']/div[@class='input-prepend']/input[@id='modlgn-username']")
usuario.send_keys("catobon")

password = controladorintranetPersonal.find_element(By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
password.send_keys("Indacoalla1988*/")

botonIngreso = controladorintranetPersonal.find_element(By.XPATH,"/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/button[1]")
botonIngreso.click()

time.sleep(5)
controladorintranetPersonal.quit()
'''
#css selector
'''
usuario = controladorintranetPersonal.find_element(By.CSS_SELECTOR, "#modlgn-username")
usuario.send_keys("catobon")

password = controladorintranetPersonal.find_element(By.CSS_SELECTOR, "#modlgn-passwd")
password.send_keys("Indacoalla1988*/")

botonIngreso = controladorintranetPersonal.find_element(By.CSS_SELECTOR,"button[name='Submit']")
botonIngreso.click()

time.sleep(5)
controladorintranetPersonal.quit()
'''
#multiples elementos

login = controladorintranetPersonal.find_elements(By.TAG_NAME, "input")

login[0].send_keys("catobon")
login[1].send_keys("Indacoalla1988*/")


botonIngreso = controladorintranetPersonal.find_element(By.TAG_NAME,"button")
botonIngreso.click()

time.sleep(5)
controladorintranetPersonal.quit()


#controlador = webdriver.Chrome()
#controlador.get("https://www.udemy.com/join/passwordless-auth/?locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2F&response_type=html&action=login&mode")


#usuario = controlador.find_element(By.ID, "form-group--1")
#usuario.send_keys("catobonpe@gmail.com")


#usuario = controlador.find_element(By.XPATH, "//input[@id='form-group--1']")
#usuario.send_keys("catobonpe@gmail.com")


#botonIngreso = controlador.find_element(By.TAG_NAME,"button")
#botonIngreso = controlador.find_element(By.CLASS_NAME,"ud-btn ud-btn-large ud-btn-brand ud-heading-md passwordless-auth-mx-code-generation-form--submit-button--2vOvZ")

#botonIngreso = controlador.find_element(By.XPATH,"//button[@class='ud-btn ud-btn-large ud-btn-brand ud-heading-md passwordless-auth-mx-code-generation-form--submit-button--2vOvZ']")

#botonIngreso.click()

#time.sleep(5)
#controlador.quit()

