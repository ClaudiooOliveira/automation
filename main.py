from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Caminho para o seu arquivo Excel (xlsx)
caminho_planilha = 'dados.xlsx'

# Carregar a planilha
planilha = pd.read_excel(caminho_planilha)

# Iniciar o navegador
driver = webdriver.Chrome()  # Certifique-se de ter o webdriver do Chrome instalado e configurado no seu sistema

# Abrir o WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Faça o login no WhatsApp Web e pressione Enter aqui depois de logado...")

while True:

    # Iterar sobre as linhas da planilha
    for indice, linha in planilha.iterrows():
        # Nome da pessoa que você deseja pesquisar
        nome_pesquisar = linha['Nome']

        # Extrair o código a ser enviado
        codigo_a_enviar = str(linha['Texto'])

        # Pesquisar o contato pelo nome
        campo_pesquisa = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/div[2]/div/div[1]'))
        )
        campo_pesquisa.send_keys(nome_pesquisar)
        time.sleep(2)
        campo_pesquisa.send_keys(Keys.RETURN)

        # Esperar um pouco antes de enviar a mensagem
        time.sleep(2)

        # Enviar a mensagem
        campo_mensagem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
        )
        campo_mensagem.send_keys(codigo_a_enviar)
        time.sleep(2)
        campo_mensagem.send_keys(Keys.RETURN)

        # Limpar o campo de pesquisa para a próxima iteração
        campo_pesquisa.clear()

        # Esperar um pouco antes de a próxima iteração
        time.sleep(2)
    
    time.sleep(10)
    

# Fechar o navegador
driver.quit()