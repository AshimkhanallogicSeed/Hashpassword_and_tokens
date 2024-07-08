from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import *
# Create your views here.

class Registeruser(APIView):
    def post(self, request):
        serializers = Userserializers(data = request.data)
        if not serializers.is_valid():
            print(serializers.errors)
            return Response({'status':403, 'serializers':serializers.errors,'message':'Invalid data'})
        serializers.save()
        user = User.objects.get(username = serializers.data['username'])
        Token_obj, _=Token.objects.get_or_create(user=user)
        return Response({'status':200, 'serializers':serializers.data,'token':str(Token_obj),'message':'User created'})
        



class userAPI(APIView):

    def get(self, request):
        pass
