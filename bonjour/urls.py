from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bonjour_index'),
    path('<str:name>', views.hello_name, name='bonjour_name'),
]
