from django.shortcuts import render
from .models import Car
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import CarSerializer


class CarCreate(generics.CreateAPIView):
    print('CREATE')
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarList(generics.ListAPIView):
    print('GET ALL')
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveAPIView):
    print('GET')
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpdate(generics.RetrieveUpdateAPIView):
    print('UPDATE')
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDelete(generics.RetrieveDestroyAPIView):
    print('DELETE')
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    