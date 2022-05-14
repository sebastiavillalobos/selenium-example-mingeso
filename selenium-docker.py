from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# print(f"El titulo de la pagina es: {driver.title}") # => "Google"
# # espera que cargue la pagina
# driver.implicitly_wait(0.5)
# driver.quit()



options = webdriver.ChromeOptions()
options.add_argument('--disable-dev-shm-usage')

# si ejecutan docker en forma local la url es: http://127.0.0.1:4444
dirver_by_docker = webdriver.Remote(command_executor="http://192.168.1.99:4444", options=options)


dirver_by_docker.get("https://www.google.com")

print(f"El titulo de la pagina es: {dirver_by_docker.title}") # => "Google"
# espera que cargue la pagina
dirver_by_docker.implicitly_wait(0.5)
dirver_by_docker.quit()