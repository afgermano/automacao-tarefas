import pyautogui
import time
import pandas as pd

#configuração de pausa(em segundos) entre as ações executadas
pyautogui.PAUSE = 3

# abrir o navegador Chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
# fazer login no sistema
time.sleep(5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)
# clicar no input de e-mail
pyautogui.click(x=449, y=411)
pyautogui.write('emailficticio@gmail.com.br')
pyautogui.press('tab')
pyautogui.write('senhaficticia')
pyautogui.press('tab')
pyautogui.press('enter')

database = pd.read_csv('produtos.csv')

for linha in database.index:
    # clicar no campo de código
    pyautogui.click(x=452, y=287)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = database.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(database.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(database.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(database.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(database.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(database.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = database.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(database.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim



