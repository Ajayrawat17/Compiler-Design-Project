from django.urls import path
from .views import CompileCodeView  # Importing the CompileCodeView

urlpatterns = [
    path('run/', CompileCodeView.as_view(), name='compile-code'),  # Define the route for compilation
]
