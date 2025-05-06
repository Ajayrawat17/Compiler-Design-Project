from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
import tempfile

# Import Python converter
from convertor.python_parser.py_converter import convert_python_to_pseudo

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Compiler backend running!"}

# Enable CORS for frontend
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
            pseudo = convert_python_to_pseudo(code)
            return {"pseudo_code": pseudo}
        except Exception as e:
            return {"error": f"Python conversion error: {str(e)}"}

    elif language.lower() == "c":
        try:
            # Save C code to a temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".c", mode="w") as temp_file:
                temp_file.write(code)
                temp_path = temp_file.name

            # Compile C parser
            subprocess.run(["make", "-C", "convertor/pseudo_parser"], check=True)

            # Use correct path separator for Windows
            binary = os.path.join("convertor", "pseudo_parser", "c_to_pseudo.exe") if os.name == 'nt' else os.path.join("convertor", "pseudo_parser", "parser")

            # Check if binary actually exists
            if not os.path.exists(binary):
                return {"error": f"Executable not found at: {binary}"}

            # Run the binary with temp file as input
            result = subprocess.run([binary, temp_path], capture_output=True, text=True)

            # Delete temp file after processing
            os.unlink(temp_path)

            return {"pseudo_code": result.stdout or "No output generated."}

        except subprocess.CalledProcessError as e:
            return {"error": f"C parser error: {e.stderr}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}

    else:
        return {"error": "Unsupported language. Please use 'python' or 'c'."}
