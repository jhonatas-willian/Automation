import pyautogui
import time
import pandas

# Passo 1 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 0.6

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("backspace")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2 - Fazer login (E-mail, Senha e Logar)
# Clicar no Email e Digitar o Email| Point(x=-2791, y=376)
pyautogui.click(x=-2791, y=376)
pyautogui.write("Jhonatas@gmail.com")

# Clicar na Senha e Digitar a Senha| Point(x=-2753, y=474)
pyautogui.click(x=-2753, y=474)
pyautogui.write("SenhaImprovavel")

# Clicar em Logar | Point(x=-2572, y=533)
pyautogui.click(x=-2572, y=533)
time.sleep(6)

# Passo 3 - Importar a base de dados com pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # Passo 4 - Cadastrar um produto
    # Código | Point(x=-2787, y=259)
    pyautogui.click(x=-2787, y=259)
    pyautogui.write(str(tabela.loc[linha, "codigo"])) # OR -> codigo = tabela.loc[linha, "coluna"]  |  pyautogui.write(codigo)
    
    # Marca | pyautogui.click(x=-2783, y=359) or
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    
    # Tipo | pyautogui.click(x=-2780, y=456) or
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    # Categoria | pyautogui.click(x=-2777, y=549) or 
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"] # OR -> pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.write(f"{categoria}")

    # Preço | pyautogui.click(x=-2778, y=649) or 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    # Custo | pyautogui.click(x=-2774, y=743) or 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    
    # OBS | pyautogui.click(x=-2777, y=847) or 
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # Se o "OBS" não for um NaN (Not a Number)
        pyautogui.write(obs)

    # Enviar | or pyautogui.click(x=-2641, y=904)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")

# Passo 5 - Repetir isso até acabar a base de dados
