from rest_framework import serializers
from .models import User,Role,UserDetails
from apps.Address.serializers import Address_seriliaztion


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password', 'avatar',
            'full_name', 'phone', 'signup_source'
        ]
        extra_kwargs = {
            'signup_source': {'default': 'website'},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value

    def validate_phone(self, value):
        if value and User.objects.filter(phone=value).exists():
            raise serializers.ValidationError('Phone number already exists')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user



class updateUserserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password', 'avatar',
            'full_name', 'phone', 'is_active'
        ]

    def validate_phone(self, value):
        user_id = self.instance.id if self.instance else None
        if value and User.objects.exclude(id=user_id).filter(phone=value).exists():
            raise serializers.ValidationError('Phone number already exists')
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
        model=Role
        fields='__all__'
        
class UserDetailsSerializer(serializers.ModelSerializer):
    user_obj=UserSerializer()
    role = RoleSerializer()
    address = Address_seriliaztion()
    reporting_to = UserSerializer()
    class Meta:
        model= UserDetails
        fields=['user_obj','role','address','reporting_to']        
