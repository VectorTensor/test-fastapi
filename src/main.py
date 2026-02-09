import random
from fastapi import FastAPI

app = FastAPI(title="Random Data API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Random Data API. Go to /random for some data."}

@app.get("/random")
def get_random_data():
    """Returns some random data."""
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    return {
        "id": random.randint(1000, 9999),
        "value": random.random(),
        "item": random.choice(items),
        "status": "success"
    }
