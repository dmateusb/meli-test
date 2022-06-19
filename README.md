# Fuego de Quasar Test

### To build and run Docker container

* docker build --tag fuego_de_quazar .
* docker run fuego_de_quazar

### To run locally

* pip3  install  -r  requirements.txt
* FLASK_APP=app.py
* flask run

### To test (with local server running)

* python3 fuego_de_quazar/tests/test_top_secret.py
