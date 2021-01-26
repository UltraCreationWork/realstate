from django.shortcuts import render,redirect
from django.core.mail import EmailMessage,send_mail
from django.template.loader import get_template
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
        "headers":Header.objects.all(),
        "aboutus":Aboutus.objects.all()[:1],
        "services":Services.objects.all(),
        "projects":Projects.objects.all(),
        "testimonials":Testimonial.objects.all(),
        "architectures":Artitecture.objects.all(),
        "contact_details":Contact_Detail.objects.all()[:1],

        }
    return render(request,"index.html",data)

# def contact(request):
#     form = ContactForm
#     if request.method == "POST":
#         if form.is_valid():
#             name = request.POST.get("name")
#             email = request.POST.get("email")
#             subject = request.POST.get("subject")
#             message = request.POST.get("message")
#             template = get_template('contact_template.txt')
#             context = {
#                 'contact_name': name,
#                 'contact_email': email,
#                 'subject': subject,
#                 'message':message,
#                 }
#             data = template.reader(context)
#             mail = EmailMessage(
#                     "New contact form submission",
#                     content,
#                     "urbanspacerealtors.com" +'',
#                     ['onlinewebsitemarket@gmail.com'],
#                     headers = {'Reply-To': email }
#                 )
#             mail.send()
#             return redirect("contact/")
#     return render(request,"index.html",{"form":form})

def contact(request):
    if request.method=="POST":
            obj = Contact()
            obj.name = request.POST.get("name")
            obj.email = request.POST.get("email")
            obj.subject = request.POST.get("subject")
            obj.message = request.POST.get("message")
            obj.save()
            send_mail(subject=obj.subject,message=obj.message,from_email="onlinewebsitemarket@gmail.com",recipient_list=[obj.email])
            send_mail(subject="reply from UrbanSpace Realtors Pvt.Ltd.",message="Thank you for contacting us",from_email="onlinewebsitemarket@gmail.com",recipient_list=[obj.email])
            return redirect("contact")
    return render(request,"index.html")
    
