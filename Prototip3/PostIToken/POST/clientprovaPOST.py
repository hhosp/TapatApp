import requests

url = "http://127.0.0.1:5000/sumar"

dades = {
    "num1": 5,
    "num2": 40
}

resposta = requests.post(url, json=dades)

if resposta.status_code == 200:
    print("Resposta: ", resposta.json())
else:
    print("Error: ", resposta.text)