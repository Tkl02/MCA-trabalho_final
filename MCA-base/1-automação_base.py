from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# dados pre-difinidos para uso  ----------------------------------------------------------------------------------------
    
email_for_login = 'diasgame006@gmail.com'
password_for_login = '**************'
title = 'reunião de tarefas do software'
date = '25/06/2023'
horario_inicial = '14:00'
horario_final = '15:00'
locations = 'goias joviania rua joao caldeira n 275'
video_chamada = 1
descrição_reuniao = 'esta reuniao consiste em definir todo o projeto do software, desde tecnologias usadas ate implementações de mercado'

# requisição de dados para uso ------------------------------------------------------------------------------------------
# email_for_login = input('digite o email de login: ')
# senha = input('digite a senha do respectivo email: ')

# title = input('digite o titulo do evento: ')
# horario = input('digite o horario na forma xx/xx/xxxx: ')
# video_chamada = int(input('digite 1 para video chamada 2 presencial: '))
# descrição_reuniao = input('descrição da reunião: ')
#location = input('localização no modelo "estado cidade rua/av/bairro num": ')

# --------------------------------------------------------------------------------------------------

# if video_chamada == 2:
#     local = input('digite a localização da reunião: ')

# lendo emails dentro do arquivo TXT
archive_emails = 'email.txt'
with open(archive_emails, 'r') as file:
    dados = file.read()
email = dados.replace("[","").replace("]","").replace("'","")

# configurando o acesso inicial do selenium
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = Chrome(options=options)

wait = WebDriverWait(driver, 10)
tempo_espera = 10
driver.get('https://accounts.google.com/ServiceLogin?hl=pt-BR&passive=true&continue=https://www.google.com.br/%3Fhl%3Dpt-BR&ec=GAZAmgQ')


# fezendo o login no google
login_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
login_email.send_keys(email_for_login + Keys.ENTER)
login_senha = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
login_senha.send_keys(password_for_login + Keys.ENTER)
time.sleep(2)

# redirecionando o site para o google agendas
driver.get('https://calendar.google.com/calendar/u/0/r?pli=1')
time.sleep(2)

# clicando no botão "Criar"
add_agenda = driver.find_element(By.CSS_SELECTOR,'body > div.tEhMVd > div.pSp5K > div.KKOvEb > div.dwlvNd')
add_agenda.click()
time.sleep(2)

# clicando no botao "evento"
add_event = driver.find_element(By.CSS_SELECTOR,'body > div.JPdR6b.QFf4q.qjTEB > div > div > span:nth-child(1) > div.uyYuVb.oJeWuf > div').click()
time.sleep(3)

# adicionando um titulo
add_tile = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/label')
add_tile.send_keys(title)

# definindo a data do evento
click_date = driver.find_element(By.CSS_SELECTOR, 'span[data-key="startDate"]').click()
time.sleep(0.8)
pyautogui.typewrite(date)
time.sleep(1)

# definendo o horario do evento
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.typewrite(horario_inicial)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.typewrite(horario_final)
pyautogui.press('enter')
time.sleep(1)

# Inserindo convidados no evento da agenda 
search_add_users = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[2]/div[1]/div[3]/div[2]/span/div/div[3]/div[1]/div/div[2]/div/button')
search_add_users.send_keys(email)
time.sleep(1)
pyautogui.typewrite(email)
time.sleep(1)
pyautogui.press('enter')


if video_chamada == 1 or video_chamada == '1':
    for _ in range(14):
        pyautogui.press('tab')
        time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.typewrite(descrição_reuniao)

elif video_chamada == 2 or video_chamada == '2':
    time.sleep(2)
    #removendo o meet clicando no "x"
    remove_meet = driver.find_element(By.CSS_SELECTOR, 'button.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.m2yD4b.GjP4J.dUoupf')
    remove_meet.click()
    time.sleep(0.5)
    #adicionando local
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(locations)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.typewrite(descrição_reuniao)
    
#salvando o evento
time.sleep(2)
save_event = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[2]/div[2]/div[4]/button')
save_event.click()
time.sleep(1)
button_element = driver.find_element(By.XPATH, '//div[contains(@class, "uArJ5e") and contains(@class, "UQuaGc") and contains(@class, "kCyAyd") and contains(@class, "l3F1ye") and contains(@class, "ARrCac") and contains(@class, "HvOprf") and contains(@class, "fY7wqd") and contains(@class, "M9Bg4d")]')
button_element.click()
time.sleep(1)

print("finalizado com sucesso.")
driver.quit()
