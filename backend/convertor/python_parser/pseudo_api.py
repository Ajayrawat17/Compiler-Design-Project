from fastapi import APIRouter
from pydantic import BaseModel
import subprocess, tempfile, os

from convertor.python_parser.py_converter import convert_python_to_pseudo

router = APIRouter()

class CodeInput(BaseModel):
    language: str
    code: str

@router.post("/convert")
def convert_code(data: CodeInput):
    if data.language.lower() == "c":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as temp:
            temp.write(data.code.encode())
            temp.flush()
            exe_path = os.path.join("backend", "convertor", "pseudo_parser", "c_to_pseudo.exe")
            result = subprocess.run([exe_path, temp.name], capture_output=True, text=True)
            return {"pseudo_code": result.stdout}
    
    elif data.language.lower() == "python":
        return {"pseudo_code": convert_python_to_pseudo(data.code)}
    
    else:
        return {"error": "Unsupported language"}
