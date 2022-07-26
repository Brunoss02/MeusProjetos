"""
Passo 1: Entrar no sistema (no nosso caso vai ser entrar no link)
Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta Exportar)
Passo 3: Download da base de dados.
Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)
Passo 5: Entrar no email.
Passo 6: Mandar um email para a diretoria com os indicadores.
"""
import pyautogui
import pyperclip
from time import sleep
import pandas

pyautogui.PAUSE = 2

# Passo 1: Entrar no sistema (no nosso caso vai ser entrar no link).

# Caso ele tiver Fechado
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

# Caso ele está aberto
# pyautogui.hotkey("ctrl", "t")

pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# site ta carregando
sleep(3)

# Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta Exportar)
pyautogui.click(x=159, y=287, clicks=2)

# Passo 3: Download da base de dados.
# pyautogui.click(x=922, y=183)

# Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)
tabela = pandas.read_excel(r"C:\Users\FamilySantos\Desktop\Projeto Python\Aula 1-20220725T231158Z-001\Aula 1\Exportar\Vendas - Dez.xlsx")
# print(pyautogui.position())
