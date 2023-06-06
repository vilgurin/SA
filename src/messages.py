from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def not_implemented():
    return "Not implemented yet"