# 1. Criar e ativar venv
### python -m venv .venv
### .\.venv\Scripts\Activate.ps1  # Windows

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Gerar Prisma Client (se schema mudou)
prisma generate

# 4. Atualizar DB (opcional)
prisma db push

# 5. Rodar o servidor
uvicorn app.main:app --reload
