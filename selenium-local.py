from selenium import webdriver
from pathlib import Path

# Path de la carpeta
current_path = Path().cwd()
# Inicia el webdriver con el chromedriver como parametro
driver = webdriver.Chrome(executable_path=f"{current_path}/chromedriver")


driver.get("https://www.google.com")
print(f"El titulo de la pagina es: {driver.title}") # => "Google"
# espera que cargue la pagina
driver.implicitly_wait(0.5)
driver.quit()