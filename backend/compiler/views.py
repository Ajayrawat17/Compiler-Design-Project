from rest_framework.views import APIView
from rest_framework.response import Response
from .compiler import run_code  # Importing the run_code function
import uuid

class CompileCodeView(APIView):
    code_storage = {}  # Dictionary to store code temporarily

    def post(self, request):
        code = request.data.get('code', '')
        language = request.data.get('language', '').lower()

        if not code or not language:
            return Response({'error': 'Code and Language are required fields.'}, status=400)
        
        # Generate unique code ID for later use
        code_id = str(uuid.uuid4())
        CompileCodeView.code_storage[code_id] = {'code': code, 'language': language}
        
        # Respond with code ID for future reference
        return Response({'code_id': code_id})

    def put(self, request):
        code_id = request.data.get('code_id', '')
        new_inputs = request.data.get('inputs', {})

        if not code_id or not new_inputs:
            return Response({'error': 'Code ID and inputs are required fields.'}, status=400)

        if code_id not in CompileCodeView.code_storage:
            return Response({'error': 'Invalid Code ID.'}, status=404)
        
        # Retrieve saved code logic
        saved_code = CompileCodeView.code_storage[code_id]['code']

        # Replace placeholders with actual inputs
        for placeholder, value in new_inputs.items():
            saved_code = saved_code.replace(f"{{{{{placeholder}}}}}", str(value))

        # Run the modified code with actual inputs
        language = CompileCodeView.code_storage[code_id]['language']
        output = run_code(language, saved_code)
        
        return Response({'output': output})
