from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request, 'main_page.html')
