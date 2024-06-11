from django.urls import path
from app2.views import register_student

urlpatterns = [
    path('', register_student, name='register_student'),
]
