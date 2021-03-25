from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('logout/', views.login_view, name='logout'),
]
