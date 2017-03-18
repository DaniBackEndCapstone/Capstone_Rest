from django.shortcuts import render
from capstone_api import serializers, models
from rest_framework import viewsets

class StateDataViewSet(viewsets.ModelViewSet):
    """
    The StateDataViewSet creates the state data view
    Author: Dani Adkins
    """
    queryset = models.StateData.objects.all()
    serializer_class = serializers.StateDataSerializer