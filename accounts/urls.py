from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.PasswordChange.as_view(), name='change-password'),
    path('password-updated/', views.PasswordResetDone.as_view(),
         name='password-updated'),
]
