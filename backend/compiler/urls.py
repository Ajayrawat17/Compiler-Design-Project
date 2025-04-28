from django.urls import path
from .views import CompileCodeView

urlpatterns = [
    path('run/', CompileCodeView.as_view(), name='compile-code'),
]
