from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

scores = []

@app.post("/score")
def save_score(data: dict):
    scores.append(data)
    return {"ok": True, "message": "Puntuación guardada"}

@app.get("/scores")
def get_scores():
    # Ordenar por puntaje descendente
    return sorted(scores, key=lambda x: x["score"], reverse=True)