from django.urls import path
from . import views

urlpatterns =[
    path('all/', views.comments_list),
    path('', views.user_comments),
    path('<int:pk>/', views.update_user_comments),
]