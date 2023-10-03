from pydantic import BaseModel

class Carro(BaseModel):
    placa: str
    modelo: str
    ano: int
