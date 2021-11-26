from logging import log
from sys import executable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")
navegador  = webdriver.Chrome(options=chrome_options)


link = 'http://127.0.0.1:5500/index.html'
navegador.get(url=link)

login = 'teste'
senha = '12345'

campo_login = navegador.find_element_by_css_selector('#login')
sleep(1)
campo_login.send_keys(login)

campo_senha = navegador.find_element_by_css_selector('#senha')
sleep(1)
campo_senha.send_keys(senha)

btn_entrar = navegador.find_element_by_css_selector('.btn')
sleep(1)
btn_entrar.click()

logado = navegador.find_elements_by_css_selector('.active')
print(logado)



sleep(3)

global getUrl
getUrl = navegador.current_url


sleep(5)
#navegador.close()

