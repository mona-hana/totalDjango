
from django.urls import include, path

from account import views



urlpatterns =[

    path('login/home/', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('signUp/', views.signUp, name='signUp'),
    path("logout_user", views.logout_user, name="logout_user"),

]


