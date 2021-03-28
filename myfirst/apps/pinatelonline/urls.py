from django.urls import path

from . import views

app_name = 'pinatelonline'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('swap', views.swap, name='swap')
]