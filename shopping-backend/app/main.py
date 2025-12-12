# app/main.py
from fastapi import FastAPI
from .db import connect, disconnect
from .routers import items, lists

app = FastAPI(title="Shopping List API")

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