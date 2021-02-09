from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])  # decorator - function is for GET method
def get_users(request):
    user_obj = User.objects.all()
    user_obj_serialized = UserSerializer(user_obj, many=True).data
    return Response(user_obj_serialized, status=HTTP_200_OK)


@api_view(['POST'])
def create_users(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    username = request.data.get('username')
    salary_per_day = request.data.get('salary_per_day')
    total_working_days = request.data.get('total_working_days')
    department = request.data.get('department')

    User(None, first_name, last_name, email, username, salary_per_day, total_working_days, department).save()

    response = {"STATUS": "YOU DID IT"}

    return Response(response, status=HTTP_200_OK)


@api_view(['GET'])
def get_salary(request, team_id):
    user_obj = User.objects.get(pk=team_id)
    monthly_salary = int(user_obj.salary_per_day) * int(user_obj.total_working_days)
    response = {"STATUS": "YOU DID IT AGAIN", "Salary": monthly_salary}

    return Response(response, status=HTTP_200_OK)
