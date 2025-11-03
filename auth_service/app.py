from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

users = {"player1": "123", "player2": "123"}

@app.post("/login")
def login(data: dict):
    user = data.get("username")
    pwd = data.get("password")
    if user in users and users[user] == pwd:
        return {"ok": True, "user": user}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")
