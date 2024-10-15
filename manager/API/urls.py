from django.urls import path, include
from rest_framework import routers
from .views import CarViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'cars/(?P<car_id>[^/.]+)/comments', CommentViewSet, basename='car-comments')

urlpatterns = [
    path('', include(router.urls)),
]
