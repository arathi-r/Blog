from django.urls import path
from . import views
urlpatterns = [
    path('', views.plist, name='plist'),
    path('pcal/',views.pcal,name='pcal'),
]