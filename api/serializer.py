from rest_framework import serializers
from .models import Book,FruitsInfo
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = [ 'username', 'password', 'email']



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitsInfo
        fields = '__all__'