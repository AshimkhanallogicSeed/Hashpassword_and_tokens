from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User




class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User    
        fields = ["username","email","password"]

   
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

