from rest_framework import serializers
from .models import User, Role, UserRole


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password', 'full_name', 'phone', 'avatar', 'gender', 'signup_source'
        ]
        extra_kwargs = {
            'signup_source': {'default': 'website'}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phone(self, value):
        if value and User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone number already exists")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name']

class updateUserserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password', 'full_name', 'phone', 'avatar', 'is_active'
        ]

    def validate_phone(self, value):
        user_id = self.instance.id if self.instance else None
        if value and User.objects.exclude(id=user_id).filter(phone=value).exists():
            raise serializers.ValidationError("Phone number already exists")
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'is_active']

class UserRoleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    role = RoleSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), write_only=True, source='role')

    class Meta:
        model = UserRole
        fields = ['user', 'role', 'user_id', 'role_id']
        # depth = 1  # optional if you want nested details

class UserProfileSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'full_name', 'phone', 'avatar', 'gender', 'is_active', 'roles']

    def get_roles(self, obj):
        user_roles = obj.roles.all()
        return [ur.role.name for ur in user_roles]

class GetAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password', 'full_name', 'phone', 'avatar', 'gender', 'signup_source']