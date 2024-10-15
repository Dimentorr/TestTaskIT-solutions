from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from cars.models import Car, CarComments
from .serializers import CarSerializer, CarCommentsSerializer


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
