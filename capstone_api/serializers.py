# from django.contrib.auth.models import User
from rest_framework import serializers
from capstone_api import models

class StateDataSerializer(serializers.HyperlinkedModelSerializer):
    """
    The StateDataSerializer
    Author: Dani Adkins
    """
    class Meta:
        model = models.StateData
        fields = '__all__'
