from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


caminho = "C:\\Users\\020125631\\Documents\\workspace\\bot_linkedin\\chromedriver.exe"
service = Service(caminho)

browser = webdriver.Chrome(service=service)

browser.get("https://www.linkedin.com/login")

input_email = browser.find_element('id', 'username').send_keys("email")
input_senha = browser.find_element('id', 'password').send_keys("senha")
botao_login = browser.find_element('xpath', "//button[@type='submit']").click()

buscaVagasPython = browser.find_element('xpath', "//input[@placeholder='Pesquisar']").send_keys("Python").send_keys(Keys.RETURN)

time.sleep(3)

filtro_vagas = browser.find_element('xpath', "//buton[@aria-label='Vagas']").click()


input('enter para fechar')