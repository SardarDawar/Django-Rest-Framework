from django.shortcuts import render

from rest_framework import generics
from .models import finder
from .serializers import FindSerializer


class ListfinderView(generics.ListAPIView):
  
    queryset = finder.objects.all()
    a=finder.TrackAddress
    serializer_class = FindSerializer
    print(a)
