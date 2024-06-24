import time
import re
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

        # Capturar o texto do elemento
        discount_text = discount_element.text

        # Usar regex para capturar o valor numérico antes de %
        match = re.search(r'(\d+)%', discount_text)
        if match:
            return int(match.group(1))
        else:
            return 0

    except Exception as e:
        print(f"Ocorreu um erro ao acessar {url}: {str(e)}")
        return 0

# Inicializar o driver do Firefox
browser = webdriver.Firefox()

# Lista para armazenar os resultados
results = []

# Abrir o arquivo usernames_and_urls.txt e processar cada linha
with open('usernames_and_urls.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Separar o username e a URL
        username, url = line.strip().split(', ')
        
        # Obter o desconto para a URL atual
        discount_value = obter_desconto(url, browser)
        
        # Adicionar o resultado à lista
        results.append(f"{username}, {url}, {discount_value}")
        
        # Aguardar um pequeno delay antes de prosseguir para a próxima URL
        time.sleep(3)  # 3 segundos de delay entre cada URL

# Fechar o navegador no final do processamento
browser.quit()

# Salvar os resultados em um novo arquivo de texto
with open('usernames_and_discounts.txt', 'w', encoding='utf-8') as output_file:
    for result in results:
        output_file.write(result + '\n')

print('Resultados salvos em usernames_and_discounts.txt.')
