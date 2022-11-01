from unicodedata import name
from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('main_erp', views.main_erp, name='home erp'),
    path('planning_erp', views.planning_erp, name='planning erp'),
    path('hr_erp', views.hr_erp, name='hr erp'),

]