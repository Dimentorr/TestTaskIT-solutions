# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

import os
import django

# Установите переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # замените 'myproject' на имя вашего проекта
django.setup()  # инициализируем Django
