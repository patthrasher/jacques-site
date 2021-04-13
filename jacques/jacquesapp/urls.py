from django.urls import path
from jacquesapp import views

app_name = 'jacquesapp'
urlpatterns = [
    path('', views.index, name='index'),
]
