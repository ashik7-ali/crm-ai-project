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

@app.post("/log-interaction")
def log_interaction(item: dict):
    data.append(item)
    return {"message": "saved", "data": item}

@app.get("/get")
def get_data():
    return data

@app.put("/edit-intraction/{index}")
def edit_interaction(index: int, item: dict):
    if index < len(data):
        data[index] = item
        return {"message": "updated"}
    return {"error": "not found"}

