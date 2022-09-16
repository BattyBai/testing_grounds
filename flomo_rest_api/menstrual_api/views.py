from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import MenstrualSerializer
from .models import Menstrual

class MenstrualList(generics.ListCreateAPIView):
    queryset = Menstrual.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = MenstrualSerializer # tell django what serializer to use

class MenstrualDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menstrual.objects.all().order_by('id')
    serializer_class = MenstrualSerializer