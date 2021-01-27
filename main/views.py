from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.views.generic import DetailView
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
    Contact_Detail,
    Footer,
    PrivancyPolicy
    )




def home(request):
    data = {
        "web_titles":website_title.objects.all()[:1],
        "headers":Header.objects.all()[:4],
        "properties":Header.objects.all(),
        "aboutus":Aboutus.objects.all()[:1],
        "services":Services.objects.all(),
        "projects":Projects.objects.all(),
        "testimonials":Testimonial.objects.all(),
        "architectures":Artitecture.objects.all(),
        "contact_details":Contact_Detail.objects.all()[:1],

        }
    return render(request,"index.html",data)


def contact(request):
    if request.method=="POST":
            obj = Contact()
            obj.name = request.POST.get("name")
            obj.email = request.POST.get("email")
            obj.mobile_no = str(+91)+request.POST.get("mobile")
            obj.subject = request.POST.get("subject")
            obj.message = request.POST.get("message")
            obj.save()
            send_mail(subject=obj.subject,message=f"My name is \'{ obj.name}\' and contact number is \'{obj.mobile_no}\' and I want to say that \'{obj.message}\'",from_email="onlinewebsitemarket@gmail.com",recipient_list="urbanspacerealtors.rkl@gmail.com")
            send_mail(subject="Reply from UrbanSpace Realtors Pvt.Ltd.",message="Thank you for contacting us",from_email="onlinewebsitemarket@gmail.com",recipient_list=[obj.email])
            return render(request,"index.html")
    return render(request,"index.html")

class header_detail_view(DetailView):
    model = Header
    template_name = "property-single.html"

    
