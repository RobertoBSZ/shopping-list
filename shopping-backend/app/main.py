# app/main.py
from fastapi import FastAPI
from .db import connect, disconnect
from .routers import items, lists
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Shopping List API")
# Para fins de teste e debug, permita TODAS as origens.
# EM PRODUÇÃO, NUNCA USE allow_origins=["*"]
origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Permite as origens da lista acima
    allow_credentials=True,            # Permite cookies de credenciais
    allow_methods=["*"],               # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],               # Permite todos os cabeçalhos
)

@app.on_event("startup")
async def on_startup():
    await connect()

@app.on_event("shutdown")
async def on_shutdown():
    await disconnect()

# incluir routers
app.include_router(lists.router, prefix="/lists", tags=["lists"])
app.include_router(items.router, prefix="/items", tags=["items"])
# app/main.py
@app.get("/")
async def root():
    return {"message": "API funcionando!"}