import tkinter as tk
from tkinter import ttk


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
    
    # Aqui você pode processar os valores recebidos como desejar
    # Por exemplo, exibi-los no console ou realizar outras ações com eles
    
    # Exemplo de exibição no console
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Title: {title}")
    print(f"Date: {date}")
    print(f"Horário inicial: {horario_inicial}")
    print(f"Horário final: {horario_final}")
    print(f"Locations: {locations}")
    print(f"Video chamada: {video_chamada}")
    print(f"Descrição da reunião: {descricao_reuniao}")
    
    # Você pode adicionar aqui a lógica para salvar os valores em algum lugar, como em um arquivo ou banco de dados
    
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

# Criando as labels e entradas de texto
email_entry = criar_label_e_input("digite o email de login:")
password_entry = criar_label_e_input("digite a senha do respectivo email:")
title_entry = criar_label_e_input("'digite o titulo do evento:")
date_entry = criar_label_e_input("digite a data na forma xx/xx/xxxx:")
horario_inicial_entry = criar_label_e_input("Horário Inicial:")
horario_final_entry = criar_label_e_input("Horário Final:")
video_chamada_entry = criar_label_e_input("digite 1 para video chamada 2 presencial:")
locations_entry = criar_label_e_input("localização no modelo 'estado cidade rua av bairro num'(caso seja via meet deixe vazia):")
descricao_reuniao_entry = criar_label_e_input("Descrição da Reunião:")

# Botão de salvar
salvar_button = ttk.Button(window, text="Salvar", command=salvar_inputs)
salvar_button.pack(pady=20)

# Executando a janela
window.mainloop()
