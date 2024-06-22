import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar o driver do Firefox
browser = webdriver.Firefox()

# URL base da primeira página
#base_url = 'https://www.vinted.pt/catalog?catalog[]=76&size_ids[]=207&brand_ids[]=88&brand_ids[]=94&brand_ids[]=304&brand_ids[]=10&brand_ids[]=11493&brand_ids[]=255&brand_ids[]=191&brand_ids[]=11421&brand_ids[]=20&brand_ids[]=120&brand_ids[]=161&price_to=5&currency=EUR&status_ids[]=6&status_ids[]=1&status_ids[]=2&order=newest_first&time=1718836305&page={}'
base_url = 'https://www.vinted.pt/catalog?size_ids[]=207&brand_ids[]=11493&currency=EUR&status_ids[]=6&status_ids[]=1&status_ids[]=2&order=newest_first&price_to=3.5&catalog[]=1809&color_ids[]=30&page={}'
# Inicializar variáveis
page_number = 0
usernames_and_urls = []

# Inicializar variáveis
page_number = 1
usernames_and_urls = []

try:
    while True:
        # Construir a URL da página atual
        url = base_url.format(page_number)
        browser.get(url)

        try:
            # Verificar se há resultados na página
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[data-testid="search-empty-state--title"]'))
            )
            empty_state_element = browser.find_element(By.CSS_SELECTOR, 'h1[data-testid="search-empty-state--title"]')
            if empty_state_element.text == 'Não foram encontrados artigos':
                print(f'Todos os artigos foram coletados. Páginas totais: {page_number - 1}')
                break
        except:
            pass

        # Esperar até que todos os elementos de nomes de utilizador e URLs estejam presentes
        username_elements = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p[data-testid$="--owner-name"]'))
        )
        url_elements = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.feed-grid__item:not(.feed-grid__item--full-row) a[href*="/member/"]'))
        )

        # Extrair os nomes de utilizador e URLs e adicionar à lista
        for username_element, url_element in zip(username_elements, url_elements):
            username = username_element.text
            profile_url = url_element.get_attribute('href')
            usernames_and_urls.append([username, profile_url])

        # Incrementar o número da página para acessar a próxima página
        page_number += 1

        # Adicionar um pequeno delay aleatório entre 1 e 3 segundos
        delay = random.uniform(1, 3)
        time.sleep(delay)

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    # Fechar o browser
    browser.quit()

    # Salvar os nomes de utilizador e URLs em um arquivo de texto
    if usernames_and_urls:
        with open('usernames_and_urls.txt', 'w', encoding='utf-8') as file:
            for username, profile_url in usernames_and_urls:
                file.write(f'{username}, {profile_url}\n')

        print(f'Nomes de utilizador e URLs salvos em usernames_and_urls.txt.')
    else:
        print('Nenhum nome de utilizador foi coletado.')