from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/games")
def list_games():
    return [{"id": 1, "title": "Coin Catcher", "description": "Atrapa monedas y evita las bombas!"}]
