from django.shortcuts import render
from .models import website_title



def home(request):
    data = {
        "web_titles":website_title.objects.all()[:1]
        }
    return render(request,"index.html",data)
    
