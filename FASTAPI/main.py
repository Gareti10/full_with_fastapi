from fastapi import FastAPI
app = FastAPI()
telefones = ['1234-5678', '9999-9999']
contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')]

contatos = dict(contatos_lista)
@app.get('/lista')
async def raizLista():
    return telefones[1]
@app.get('/dicionario') 
async def raizDict (): 
    return contatos['Ana']

if __name__ == '__main__' :
    import uvicorn 
    uvicorn.run("main:app", host="0.0.0.0", port =8000, reload = True)