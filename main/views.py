from django.shortcuts import render
from .models import ( 
    website_title,
    Header,
    Aboutus,
    Feature,
    Services,
    Projects,
    Testimonial,
    Price,
    FAQ,
    Artitecture,
    Contact,
    Footer,
    PrivancyPolicy
    )




def home(request):
    data = {
        "web_titles":website_title.objects.all()[:1],
        "headers":Header.objects.all(),

        }
    return render(request,"index.html",data)
    
