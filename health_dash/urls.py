from django.urls import path
from .views import healthDash,qb,interface

urlpatterns = [
    path('', healthDash, name='health-dash'),
    path('test', qb),
    path('interface', interface)
]