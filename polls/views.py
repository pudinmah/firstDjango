from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Halo Mahpudin Anda sedang belajar django selamat !!!")