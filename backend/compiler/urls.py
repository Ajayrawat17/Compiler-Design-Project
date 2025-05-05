from django.urls import path
from .views import CompileCodeView

urlpatterns = [
    path('run/', CompileCodeView.as_view(), name='compile-code'),  # POST request for compiling code
    path('update/', CompileCodeView.as_view(), name='update-code'),  # PUT request for updating code
]
