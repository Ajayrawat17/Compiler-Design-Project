from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from converters.c_to_pseudo import convert_c_to_pseudocode
from converters.python_to_pseudo import convert_python_to_pseudocode

app = FastAPI(title="Pseudocode Converter API", version="1.0")

class CodeRequest(BaseModel):
    language: str  # 'c' or 'python'
    code: str

@app.post("/convert", summary="Convert C/Python code to Pseudocode")
def convert_code(request: CodeRequest):
    if request.language.lower() == "c":
        return {"pseudocode": convert_c_to_pseudocode(request.code)}
    elif request.language.lower() == "python":
        return {"pseudocode": convert_python_to_pseudocode(request.code)}
    else:
        raise HTTPException(status_code=400, detail="Only 'c' and 'python' are supported.")
