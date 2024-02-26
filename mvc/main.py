from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from time import sleep
from models import Tenis
from models import ltenis


def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)

app = FastAPI(
    title='API de Tenis',
    version='0.0.1',
    description='Uma API Fast'
)

@app.get('/tenis',
         description='Retorna todos os tenis ou uma lista vazia.',
         summary='Retorna todos os tenis',
         response_model=List[Tenis],
         response_description='Tenis encontrados com sucesso.')
async def get_viagens(db: Any = Depends(fake_db)):
    return ltenis

@app.post('/tenis', status_code=status.HTTP_201_CREATED, response_model=Tenis)
async def post_tenis(tenis: Tenis):
    next_id: int = len(ltenis) + 1
    tenis.id = next_id
    ltenis.append(tenis)
    return tenis

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
