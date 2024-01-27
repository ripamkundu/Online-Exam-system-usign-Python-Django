from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    # path('', views.index,name="index"),
    # path('login/', views.login,name="login"),
    path('login/startexam/', views.startexam,name="startexam"),
    # path('login/saveans/', views.SaveAns,name="saveans"),
    # path('endexam/', views.endexam,name="endexam"),
    path('login/startexam/<str:q_id>/', views.basic,name="basic"),
    path('login/saveans/<str:q_id>/', views.saveans,name="saveans"),\
    path('login/question/<str:q_id>/', views.travelAns,name="travelAns"),
    path('login/startexam/<str:q_id>/endpage/', views.endpage,name="endpage"),
    # path('login/startexam/q2/', views.q2,name="q2"),
]
