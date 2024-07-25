from fastapi import FastAPI
from enum import Enum

class Symbols(str, Enum):
    """Enumeratie van verschillende symbols"""
    jpy = "JPY"
    eur = "EUR"
    usd = "USD"

app = FastAPI()


@app.get("/foo")
async def root():
    return  {"msg":"bla"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item_id = item_id.split("_")
    return "__bla__".join(item_id)

@app.get("/symbols/{symbol_name}")
async def get_model(symbol_name: Symbols):
    if symbol_name is Symbols.jpy:
        return {"symbol_name": symbol_name, "message": "japanese yen"}

    if symbol_name == "EUR":
        return {"symbol_name": symbol_name, "message": "europese euro"}

    return {"symbol_name": symbol_name, "message": "waarschijnlijk USD"}

@app.get("/params/{stringetje}")
async def return_string(stringetje: str, repeats: int = 2):
    return {"string": stringetje * repeats}

@app.get("/symbols/{symbol_name}/params/{stringetje}")
async def return_string(symbol_name : str, stringetje: str, repeats: int = 2):
    if symbol_name is Symbols.jpy:
        return "japanese yen" + stringetje * repeats

    if symbol_name == "EUR":
        return  "europese euro" + stringetje * repeats

    return {"symbol_name": symbol_name, "message": "waarschijnlijk USD?" + stringetje * repeats}