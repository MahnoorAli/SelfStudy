from django.urls import path
from .views import *

urlpatterns = [
    path('Users', get_users),
    path('Save', create_users),
    path('Salary/<int:team_id>', get_salary),
]
