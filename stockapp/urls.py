from django.urls import path
from . import views

app_name = 'Stockapp'

urlpatterns = [
    path('index/', views.indexpage, name="indexpage"),
]