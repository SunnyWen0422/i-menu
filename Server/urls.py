from django.urls import path
from django.views.generic import TemplateView
from . import views
# now import the views.py file into this code
urlpatterns = [
    path("get/", views.get_menu),
    path('get/get_menu', views.result, name='result'),
    path(' ', TemplateView.as_view(template_name='index.html'), name='index'),
]
