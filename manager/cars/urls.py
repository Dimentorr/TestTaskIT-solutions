from django.urls import path
from . import views

urlpatterns = [
    path('<int:car_id>', views.car_info, name='car_info'),
]