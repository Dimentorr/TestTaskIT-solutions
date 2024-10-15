from django.urls import path, include
from rest_framework import routers
from .views import CarViewSet, CommentViewSet
from .views import get_token

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'cars/(?P<car_id>[^/.]+)/comments', CommentViewSet, basename='car-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('get_token/', get_token, name='get_token'),
]
