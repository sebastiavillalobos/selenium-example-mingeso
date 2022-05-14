# Selenium
+ [ ] [SELENIUM WEB](https://www.selenium.dev/documentation/overview/)

## crear virtual env
```python
# Instalar virtualenv
pip3 install virtualenv
# Crear e iniciar virtualenv
virtualenv -p python3 $PWD && source $PWD/bin/activate
```
## Instalar librerias
```python
pip3 install selenium
pip3 install webdriver-manager
```
## Descargar chromedriver
Segun la version de chrome instalada localmente
+ [ ] https://chromedriver.chromium.org/downloads

## Agregar al Path
Agregar el path de ubicacion del chromedriver al PATH
```
export PATH="$PWD:$PATH"
```
o utilizar python para cargar el archivo.
## Ejecutar script
```
python3 selenium-local.py
```


## DOCKER
Iniciar selenium utilizando la ultimima version con chrome disponible, descargandola desde [docker hub](https://hub.docker.com/r/selenium/standalone-chrome)
```
docker run -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.1.4-20220427
```
## Ejecutar script
```
python3 selenium-docker.py
```

## Referencias

  + [Web elements](https://www.selenium.dev/documentation/webdriver/elements/): Identifying and working with element objects in the DOM.
  + [GitHub Docker Selenium](https://github.com/SeleniumHQ/docker-selenium) Repositorio