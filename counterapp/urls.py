from django.urls import path
from . import views 


urlpatterns = [
    path ('increment/', views.increment, name='increment'),
    path ('', views.helloworld, name='helloworld'),
    path ('hellostudent/', views.hellostudent, name='hellostudent'), 
    path ('decrement/', views.decrement, name='decrement'),
    path ('reset/', views.reset, name='reset'),
   
]
