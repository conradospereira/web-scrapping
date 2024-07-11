from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Configuração do Selenium
driver = webdriver.Chrome()  # Você pode mudar o driver de acordo com seu navegador

try:
    # Abre a página de login
    driver.get("https://www.clubedepromos.com.br/#/minoristas/promociones/listado?vigente=1&estado=PENDIENTE")

    # Aguarda até que o campo de usuário seja visível e preenche
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
    )
    username.send_keys("DSOUZA")

    # Aguarda até que o campo de senha seja visível e preenche
    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]'))
    )
    password.send_keys("DIEGO24997")

    # Envia o formulário de login pressionando Enter no campo de senha
    password.send_keys(Keys.ENTER)

    link_radio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "#/minoristas/promociones/listado?vigente=1&estado=ACEPTADA")]'))
    )
    link_radio.click()
    #<a _ngcontent-xrk-c12="" href="#/minoristas/promociones/listado?vigente=1&amp;estado=ACEPTADA"><input _ngcontent-xrk-c12="" class="e2e-estado-radiobutton" type="radio" id="ACEPTADA"><label _ngcontent-xrk-c12="" for="ACEPTADA"> Aceita <!----><span _ngcontent-xrk-c12="" class="cantidad text-size-xs-cpm ng-star-inserted">(84)</span></label></a>

    #link_produto = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, '//a[@class="e2e-btn-redireccionar"]'))
    #)
    #link_produto.click()
    #<a _ngcontent-xrk-c26="" class="e2e-btn-redireccionar" href="#/minoristas/promociones/ofrecidas/1405078"><h3 _ngcontent-xrk-c26="" class="titulo-sm font-w-700-cpm mt-0 mb-0">POR R$ 12,45 NO AMACIANTE COMFORT 500ML</h3></a>
    
    # Aguarda até que o elemento esteja visível após o login
    gtins = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "font-w-500-cpm")]'))
    )

    # Itera sobre os spans e imprime seus textos
    for span in gtins:
        print("Texto do span:", span.text)

finally:
    # Fecha o navegador
    driver.quit()
