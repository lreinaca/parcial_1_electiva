
from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def get_info():
    return {
        "action1": "CREATE",
        "action2": "READ",
        "action3": "UPDATE",
        "action4": "DELETE",
        "action5": "EXIT"
    }

# Ejecutar con: uvicorn main:app --reload
               