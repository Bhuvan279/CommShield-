from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import *

from .serializers import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['POST'])
def addUser(request):

    serializer = ProfileSerializer(data=request.data)

    if serializer.is_valid():
        print(serializer.data)
        user1 = Profile.objects.filter(phone_number=serializer.data['phone_number'])
        if(user1):
            print('Someone with same number exists')
            print(user1)
        else:
            user = serializer.data.get('user')
            zip_code = serializer.data.get('zip_code')
            phone_number = serializer.data.get('phone_number')
            profile = Profile(user=user,phone_number = phone_number ,zip_code=zip_code)
            profile.save()
            print('No one exists')
        
    
    return Response(serializer.data)

@api_view(['GET'])
def showUsers(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def showUsersInZip(request,pk):
    profiles = Profile.objects.filter(zip_code=pk)
    serializer = ProfileSerializer(profiles, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def showVictimsInfo(request):
    missing = Missing.objects.all()
    serializer = MissingSerializer(missing, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def postVictimsInfo(request):

    print(request.data)
    serializer = MissingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    profiles_in_area = Profile.objects.filter(zip_code = request.data['last_seen_zip_code'])
    serializer_2 = ProfileSerializer(profiles_in_area, many=True)
    
    return Response(serializer_2.data)