
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = []

@app.get("/status")
def status():
    return {"status": "running", "stored_values": len(data)}

@app.post("/add/{value}")
def add_value(value: float):
    data.append(value)
    return {"status": "ok", "total": len(data)}

@app.post("/reset")
def reset():
    data.clear()
    return {"status":"reset"}

@app.get("/predict")
def predict():
    if not data:
        return {"error":"no data"}
    threshold = 2.0
    prob = len([x for x in data if x >= threshold]) / len(data)
    return {"probability_over_2x": prob}
