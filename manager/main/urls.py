from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<token>', views.index, name='home'),
]