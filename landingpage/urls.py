from django.urls import path
from . import views

app_name = 'landingpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_view, name='form_view'),

]
