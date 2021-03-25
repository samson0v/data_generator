from django.urls import path

from . import views


app_name = 'welcome_page'

urlpatterns = [
    path('', views.WelcomePageView.as_view(), name='welcome-page'),
]
