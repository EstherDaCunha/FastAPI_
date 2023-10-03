from fastapi import FastAPI
import requests
import random
import refactored_database

app = FastAPI()

@app.get("/carros")
async def get_carros():
    carros = refactored_database.get_carros()
    return {"message": carros}

@app.get("/carros/{placa}")
async def modelos(placa: str):
    url = f'https://wdapi2.com.br/consulta/{placa}/45147327cb7c0a2a37727a6555fc7879'
    req = requests.get(url)
    return req.json()

@app.post("/create")
async def criar(novo_carro: refactored_database.Carro):
    refactored_database.create_carro(novo_carro)
    return {"message": "Carro created", "data":novo_carro}

@app.put("/update/{placa}")
async def atualizar(placa: str, carro: Carro):
    carros[placa] = carro
    return carro

@app.delete("/delete/{placa}")
async def deletar(placa: str):
    del carros[placa]
    return {"message": "Item deletado"}

@app.get("/dog")
async def get_dog():
    id = random.randint(1, 266)
    url = f"http://10.234.82.137:8011/dogs/{id}"
    request = requests.get(url)
    return request.json()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
