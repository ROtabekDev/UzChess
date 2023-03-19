from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rest_framework.exceptions import AuthenticationFailed

from .models import (
    User,
)
 

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.DictField(source='tokens', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name',  'last_name', 'phone_number', 'password', 'password2', 'token')
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Parollar bir xil emas.'})
        
        del password2

        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer): 
    phone_number = serializers.CharField(max_length=15) 
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True) 

    class Meta:
        model = User
        fields = ('id', 'first_name',  'last_name', 'phone_number', 'password', 'tokens')

    def validate(self, attrs): 
        phone_number = attrs.get('phone_number', '')
        password = attrs.get('password', '')

        user = authenticate(phone_number=phone_number, password=password)  
 
        if not user:
            raise AuthenticationFailed({
                'message': 'Telefon nomer yoki parol noto`g`ri yoki foydalanuvchi faol emas.'
            })

        return {
            "first_name": user.first_name, 
            "last_name": user.last_name, 
            'phone_number': user.phone_number, 
            'tokens': user.tokens
        } 