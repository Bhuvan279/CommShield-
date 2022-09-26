from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'

class MissingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missing
        fields = '__all__'