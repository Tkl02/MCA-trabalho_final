from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

email_for_login = 'diasgame006@gmail.com'
password_for_login = 'diasgamerbr0220'

driver = Chrome()
wait = WebDriverWait(driver, 10)

driver.get('https://accounts.google.com/ServiceLogin?hl=pt-BR&passive=true&continue=https://www.google.com.br/%3Fhl%3Dpt-BR&ec=GAZAmgQ')

# fazendo login no google
tempo_espera = 10

# Encontrar o elemento de e-mail
login_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
login_email.send_keys(email_for_login + Keys.ENTER)


login_senha = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
login_senha.send_keys(password_for_login + Keys.ENTER)

time.sleep(2)

driver.get('https://calendar.google.com/calendar/u/0/r?pli=1')
time.sleep(2)


//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[2]/div[1]/div[3]/div[2]/span/div/div[5]/div[1]/div/div[2]/div/button


input("Pressione qualquer tecla para sair...")
driver.quit()