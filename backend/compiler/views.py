from rest_framework.views import APIView
from rest_framework.response import Response
from .compiler import run_code  # Importing the run_code function

class CompileCodeView(APIView):
    def post(self, request):
        code = request.data.get('code', '')
        language = request.data.get('language', '').lower()

        if not code or not language:
            return Response({'error': 'Code and Language are required fields.'}, status=400)

        output = run_code(language, code)
        return Response({'output': output})
