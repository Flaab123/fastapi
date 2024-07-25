from fastapi import FastAPI

app = FastAPI()


@app.get("/foo")
async def root():
    return {"message": "Hello World"}