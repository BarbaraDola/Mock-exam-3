from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def main_view(request):
    if request.method == "GET":
        return render(request, 'main_page.html')
