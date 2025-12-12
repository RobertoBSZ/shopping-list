# app/db.py
from prisma import Prisma

prisma = Prisma()  # async client (interface asyncio por generator)

async def connect():
    await prisma.connect()

async def disconnect():
    await prisma.disconnect()
