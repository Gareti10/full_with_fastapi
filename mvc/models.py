from typing import Optional
from pydantic import BaseModel, validator

class Tenis(BaseModel):
    id: Optional[int] = None
    sexo: str
    tamanho: int  
    cor: str 

    @validator('sexo')
    def validar_sexo(cls, value: str):
        # Validacao 1
        if value != "Masculino":
            print("Esta área é destinada a tenis masculino.")
            raise ValueError('Esta área é destinada a tenis masculino.')
        # Validacao 2
        if value.islower():
            print("A descrição deve ser capitalizada")
            raise ValueError('A descrição deve ser capitalizada.')
        return value
ltenis = [
    Tenis(id=1, sexo='Masculino', tamanho=41, cor="azul"),
    Tenis(id=2, sexo='Masculino', tamanho=40, cor="Branco"),
]

