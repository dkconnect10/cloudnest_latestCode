from rest_framework import serializers
from .models import Hospital, UserHospital
from apps.users.models import User, Role, UserRole

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        read_only_fields = ['id', 'owner']

class HospitalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHospital
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'user_email', 'role', 'role_name']

class HospitalDetailSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True, source='users')

    class Meta:
        model = Hospital
        fields = '__all__'
