from django.urls import path
from . import views 


urlpatterns = [
    path ('todoview/', views.todoview, name='todoview'),
    path ('todoview/addtask/', views.addtask, name='addtask' ),
]
