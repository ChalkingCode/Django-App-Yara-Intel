from django.shortcuts import render

# Create your views here.
from .models import Adrule
from .serializers import AdruleSerializer
from rest_framework import generics

class AdruleList(generics.ListCreateAPIView):
    queryset = Adrule.objects.all()
    serializer_class = AdruleSerializer

class AdruleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adrule.objects.all()
    serializer_class = AdruleSerializer