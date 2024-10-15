from django.shortcuts import redirect

from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from cars.models import Car, CarComments
from .serializers import CarSerializer, CarCommentsSerializer

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CarCommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        car_id = self.kwargs['car_id']
        return CarComments.objects.filter(car_id=car_id)

    def perform_create(self, serializer):
        car_id = self.kwargs['car_id']
        car = Car.objects.get(pk=car_id)
        serializer.save(car=car, owner=self.request.user)


def create_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key


def get_token(request):
    if request.user.is_authenticated:
        print("Token created")
        token = create_token(request.user)
        print(token)
    return redirect('home', token=token)
