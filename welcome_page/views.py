from django.shortcuts import render
from django.views.generic import TemplateView


class WelcomePageView(TemplateView):
    template_name = 'welcome_page/index.html'
