from django.urls import path
from .import views


app_name = 'my_portfolio'

urlpatterns = [
	path('',views.index,name='index'),
]	