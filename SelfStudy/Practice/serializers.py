# serializers - to convert objects to JSON

from rest_framework import serializers
from .models import User, Department


class UserSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ('team_id', 'first_name', 'last_name', 'department', 'salary_per_day', 'total_working_days')
