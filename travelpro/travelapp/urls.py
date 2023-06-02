
from django.contrib import admin
from django.urls import path

from travelapp import views

app_name='travelapp2'

urlpatterns = [
        path('', views.web1,name='web1'),

]
