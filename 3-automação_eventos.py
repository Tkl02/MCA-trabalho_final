from tkinter import filedialog
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ___________________________________________________ CONSIDERAÇÕES _______________________________________________________
# 1. Para o funcionamento da automação, digite os dados de acordo com os exemplos.
# 2. Caso os dados sejam digitados incorretamente, a automação não funcionará e você terá que verificar e corrigir os dados.
# 3. Caso a interface seja fechada automaticamente, isso indica que a execução foi bem-sucedida.
# -----------------------------------------------------------------------------------------------------------------------

def criar_evento(email_for_login, password_for_login, title, date, horario_inicial, horario_final, locations, video_chamada, descricao_reuniao):
    # Configurando o acesso inicial do selenium
    driver = Chrome()
    wait = WebDriverWait(driver, 10)
    tempo_espera = 10
    driver.get('https://accounts.google.com/ServiceLogin?hl=pt-BR&passive=true&continue=https://www.google.com.br/%3Fhl%3Dpt-BR&ec=GAZAmgQ')

    # Fazendo a leitura dos emails
    archive_emails = file_path
    with open(archive_emails, 'r') as file:
        dados = file.read()
    email = dados.replace("[", "").replace("]", "").replace("'", "")

    # Fazendo o login no Google
    login_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
    login_email.send_keys(email_for_login + Keys.ENTER)
    login_senha = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    login_senha.send_keys(password_for_login + Keys.ENTER)
    time.sleep(2)

    # Redirecionando o site para o Google Agenda
    driver.get('https://calendar.google.com/calendar/u/0/r?pli=1')
    time.sleep(2)

    # Clicando no botão "Criar"
    add_agenda = driver.find_element(By.CSS_SELECTOR, 'body > div.tEhMVd > div.pSp5K > div.KKOvEb > div.dwlvNd')
    add_agenda.click()
    time.sleep(2)

    # Clicando no botão "evento"
    add_event = driver.find_element(By.CSS_SELECTOR, 'body > div.JPdR6b.QFf4q.qjTEB > div > div > span:nth-child(1) > div.uyYuVb.oJeWuf > div')
    add_event.click()
    time.sleep(3)

    # Adicionando um título
    add_tile = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/label')
    add_tile.send_keys(title)

    # Definindo a data do evento
    click_date = driver.find_element(By.CSS_SELECTOR, 'span[data-key="startDate"]')
    click_date.click()
    time.sleep(0.8)
    pyautogui.typewrite(date)
    time.sleep(1)

    # Definindo o horário do evento
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

    if video_chamada == '1':
        for _ in range(14):
            pyautogui.press('tab')
            time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.typewrite(descricao_reuniao)

    elif video_chamada == '2':
        time.sleep(2)
        # Removendo o meet clicando no "x"
        remove_meet = driver.find_element(By.CSS_SELECTOR, 'button.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.m2yD4b.GjP4J.dUoupf')
        remove_meet.click()
        time.sleep(0.5)
        # Adicionando local
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.typewrite(locations)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.typewrite(descricao_reuniao)

    # Salvando o evento
    time.sleep(4)
    save_event = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[2]/div[2]/div[4]/button')
    save_event.click()
    time.sleep(1.5)
    button_element = driver.find_element(By.XPATH, '//div[contains(@class, "uArJ5e") and contains(@class, "UQuaGc") and contains(@class, "kCyAyd") and contains(@class, "l3F1ye") and contains(@class, "ARrCac") and contains(@class, "HvOprf") and contains(@class, "fY7wqd") and contains(@class, "M9Bg4d")]')
    button_element.click()
    time.sleep(2)

    print("Finalizado com sucesso.")
    driver.quit()

import tkinter as tk
from tkinter import ttk

file_path = ""

def selecionar_arquivo():
    global file_path
    file_path = filedialog.askopenfilename()

# Função que guardará os dados inseridos na interface
def salvar_inputs():
    email = email_entry.get()
    password = password_entry.get()
    title = title_entry.get()
    date = date_entry.get()
    horario_inicial = horario_inicial_entry.get()
    horario_final = horario_final_entry.get()
    locations = locations_entry.get()
    video_chamada = video_chamada_entry.get()
    descricao_reuniao = descricao_reuniao_entry.get()
    criar_evento(email, password, title, date, horario_inicial, horario_final, locations, video_chamada, descricao_reuniao)
    # Fechando a janela após salvar os inputs
    window.destroy()


# Criação da janela
window = tk.Tk()
window.title("Inputs")
window.configure(bg="black")  # Definindo o tema "dark"
window.geometry("700x500")  # Definindo o tamanho da janela

# Função para centralizar e definir o tamanho da janela
def configurar_janela(janela):
    largura_janela = 770
    altura_janela = 740
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posicao_x = int((largura_tela / 2) - (largura_janela / 2))
    posicao_y = int((altura_tela / 2) - (altura_janela / 2))
    janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


configurar_janela(window)

# Estilo para aumentar o tamanho da fonte
fonte = ("Arial", 14)

# Função para criar uma label com uma entrada de texto
def criar_label_e_input(texto):
    label = ttk.Label(window, text=texto, font=fonte, foreground="white", background="black")
    label.pack(pady=10)
    entry = ttk.Entry(window, width=60, font=fonte)
    entry.pack()
    return entry

# Função para criar uma label específica da senha com máscara
def label_e_password(texto):
    label = ttk.Label(window, text=texto, font=fonte, foreground="white", background="black")
    label.pack(pady=10)
    entry = ttk.Entry(window, width=60, font=fonte, show="$")
    entry.pack()
    return entry

# Criando as labels e entradas de texto
email_entry = criar_label_e_input("EMAIL")
password_entry = label_e_password("PASSWORD")
title_entry = criar_label_e_input("Titulo do Evento")
date_entry = criar_label_e_input("Data (xx/xx/xxxx)")
horario_inicial_entry = criar_label_e_input("Horário Inicial (xx:xx) :")
horario_final_entry = criar_label_e_input("Horário Final (xx:xx)")
video_chamada_entry = criar_label_e_input("Digite 1 para video chamada ou 2 para presencial:")
locations_entry = criar_label_e_input("Localização no modelo 'estado cidade rua av bairro num' (caso seja via meet deixe vazia):")
descricao_reuniao_entry = criar_label_e_input("Descrição da Reunião:")

# Botão para selecionar arquivo
selecionar_arquivo_button = ttk.Button(window, text="SELECIONAR EMAILS", command=selecionar_arquivo)
selecionar_arquivo_button.pack(side="left", padx=20, pady=20)

# Botão de salvar
salvar_button = ttk.Button(window, text="Start", command=salvar_inputs)
salvar_button.pack(side="right", padx=30, pady=20)

# Botão de automação avançada
# salvar_button = ttk.Button(window, text="AUTOMAÇÃO AVANÇADA", command=salvar_inputs)
# salvar_button.pack(padx=30, pady=20)

# Executando a janela
window.mainloop()
