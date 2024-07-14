import os
import toml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Define o caminho para o arquivo .toml
SECRETS_FILE = os.path.join('secrets.toml')

# Carrega as variáveis do arquivo .toml
with open(SECRETS_FILE, 'r') as f:
    secrets = toml.load(f)

# Verifica se as chaves 'credentials', 'username' e 'password' existem no dicionário
if 'credentials' in secrets and 'username' in secrets['credentials'] and 'password' in secrets['credentials']:
    user = secrets['credentials']['username']
    password_value = secrets['credentials']['password']
else:
    raise KeyError("As chaves 'credentials', 'username' ou 'password' não foram encontradas no arquivo .toml.")

# Configuração do Selenium
driver = webdriver.Chrome()  # Você pode mudar o driver de acordo com seu navegador

try:
    # Abre a página de login
    driver.get("https://www.clubedepromos.com.br/#/minoristas/promociones/listado?vigente=1&estado=PENDIENTE")

    # Aguarda até que o campo de usuário seja visível e preenche
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
    )
    username_input.send_keys(user)

    # Aguarda até que o campo de senha seja visível e preenche
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]'))
    )
    password_input.send_keys(password_value)

    # Envia o formulário de login pressionando Enter no campo de senha
    password_input.send_keys(Keys.ENTER)

    # Aguarda até que o link do estado 'ACEPTADA' esteja visível e clica nele
    link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='#/minoristas/promociones/listado?vigente=1'][href*='estado=ACEPTADA']"))
    )
    link_element.click()
    #<a _ngcontent-xrk-c12="" href="#/minoristas/promociones/listado?vigente=1&amp;estado=ACEPTADA"><input _ngcontent-xrk-c12="" class="e2e-estado-radiobutton" type="radio" id="ACEPTADA"><label _ngcontent-xrk-c12="" for="ACEPTADA"> Aceita <!----><span _ngcontent-xrk-c12="" class="cantidad text-size-xs-cpm ng-star-inserted">(84)</span></label></a>

    # Aguarda até que os spans estejam visíveis após o clique na promoção
    gtins = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "font-w-500-cpm")]'))
    )

    # Itera sobre os spans e imprime seus textos
    for span in gtins:
        print("Texto do span:", span.text)

    # Volta uma página
    driver.back()

finally:
    # Fecha o navegador
    driver.quit()
