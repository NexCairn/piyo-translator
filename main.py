from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from piyo.core import PiyoTranslator
import os

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    action: str  # "encode" or "decode"

@app.post("/api/translate")
async def translate(request: TranslationRequest):
    try:
        if request.action == "encode":
            result = PiyoTranslator.encode(request.text)
        elif request.action == "decode":
            result = PiyoTranslator.decode(request.text)
        else:
            raise HTTPException(status_code=400, detail="Invalid action. Must be 'encode' or 'decode'.")
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")
