from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
import tempfile

# Correct function name - adjust if needed in py_converter.py
from convertor.python_parser.py_converter import convert_to_pseudocode

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Compiler backend running!"}

# Enable CORS so frontend can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/convert/")
async def convert_code(language: str = Form(...), code: str = Form(...)):
    if language.lower() == "python":
        try:
            pseudo = convert_to_pseudocode(code)
            return {"pseudo_code": pseudo}
        except Exception as e:
            return {"error": f"Python conversion error: {str(e)}"}

    elif language.lower() == "c":
        try:
            # Save C code to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".c", mode="w") as temp_file:
                temp_file.write(code)
                temp_path = temp_file.name

            # Run make to compile C parser (only once ideally, can optimize this later)
            subprocess.run(["make", "-C", "convertor/pseudo_parser"], check=True)

            # Choose correct executable based on OS
            binary = os.path.join("convertor", "pseudo_parser", "c_to_pseudo.exe") if os.name == 'nt' else os.path.join("convertor", "pseudo_parser", "parser")

            if not os.path.exists(binary):
                return {"error": f"Executable not found at: {binary}"}

            # Execute binary with the temp file as input
            result = subprocess.run([binary, temp_path], capture_output=True, text=True)

            # Clean up temp file
            os.unlink(temp_path)

            return {"pseudo_code": result.stdout or "No output generated."}

        except subprocess.CalledProcessError as e:
            return {"error": f"C parser error: {e.stderr}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}

    else:
        return {"error": "Unsupported language. Please use 'python' or 'c'."}
