import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para obter o desconto de uma URL específica
def obter_desconto(url, browser):
    try:
        # Acessar o URL do perfil
        browser.get(url)

        # Esperar até que o elemento h3 com o texto desejado esteja presente
        discount_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.web_ui__Cell__navigating:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1)'))
        )

        # Retornar o texto do elemento
        return discount_element.text

    except Exception as e:
        print(f"Ocorreu um erro ao acessar {url}: {str(e)}")
        return None

# Inicializar o driver do Firefox
browser = webdriver.Firefox()

# Abrir o arquivo usernames_and_urls.txt e processar cada linha
with open('usernames_and_urls.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Separar o username e a URL
        username, url = line.strip().split(', ')
        
        # Obter o desconto para a URL atual
        discount_text = obter_desconto(url, browser)
        
        # Imprimir o resultado
        if discount_text:
            print(f"{username} - Desconto: {discount_text}")
        
        # Aguardar um pequeno delay antes de prosseguir para a próxima URL
        time.sleep(3)  # 3 segundos de delay entre cada URL

# Fechar o navegador no final do processamento
browser.quit()
