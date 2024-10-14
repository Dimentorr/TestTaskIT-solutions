from django.urls import path
from . import views

urlpatterns = [
    path('<int:car_id>', views.car_info, name='car_info'),
    path('edit_commit/<int:commit_id>', views.edit_commit, name='edit_commit'),
    path('send_commit/<int:car_id>/<int:author_id>/<str:commit>', views.send, name='car_commit_send'),
    path('car_create', views.car_create, name='car_create'),
    path('car_update/<int:car_id>', views.car_update, name='car_update'),
]