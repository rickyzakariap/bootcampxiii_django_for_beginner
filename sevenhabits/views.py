from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from sevenhabits.models import Roles, Goals
from sevenhabits.serializers import GoalsSerializer, RolesSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class GoalsViewSet(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
