from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.core.mail import send_mail
from django.template.loader import get_template
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    PrivacyPolicy,
    Career,
    Career_header,
    Blog,
    Past_Projects,
    Current_Projects,
    Proposed_Projects,
    Comment,
    Current_Projects_description,
    Past_Projects_description,
    Proposed_Projects_description
    )

import random


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
        "pricing":Price.objects.all(),

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
            send_mail(subject=obj.subject,message=f"My name is \'{ obj.name}\' and contact number is \'{obj.mobile_no}\' and I want to say that \'{obj.message}\'",from_email="urbanspacerealtors.rkl@gmail.com",recipient_list=["rahulsinha.arch@gmail.com"])
            send_mail(subject="Reply from UrbanSpace Realtors Pvt.Ltd.",message="Thank you for contacting us",from_email="urbanspacerealtors.rkl@gmail.com",recipient_list=[obj.email])
            return render(request,"index.html")
    return render(request,"index.html")

class header_detail_view(DetailView):
    model = Header
    template_name = "property-single.html"


def privacypolicy(request):
    data = {
        "privacypolicies" :PrivacyPolicy.objects.all()[:1]
    }
    return render(request,"privacy.html",data)

def testimonal_add(request):
    if request.method == "POST":
        obj = Testimonial()
        obj.name = request.POST.get("name")
        obj.prop_img = request.FILES.get("prop_img")
        obj.img = request.FILES.get("img")
        obj.prof = request.POST.get("prof")
        obj.disc = request.POST.get("disc")
        obj.social_link_f = request.POST.get("facebook")
        obj.social_link_t = request.POST.get("twitter")
        obj.social_link_i = request.POST.get("instagram")
        obj.social_link_l = request.POST.get("linkedin")
        obj.save()
        return render(request,"thankyou.html")
    return render(request,"testimonialform.html")

class Project_detail(DetailView):
    template_name="project.html"
    model = Projects

def carrier(request):
    data = { 
        "careers":Career.objects.all(),
        "career_header":Career_header.objects.all()[:1]
     }
    return render(request,"career.html",data)

class Carrier_detail(DetailView):
    template_name = "career_detail.html"
    model = Career


def portfollio(request):
    data = {
        "proposed":Proposed_Projects.objects.all(),
        "past":Past_Projects.objects.all(),
        "current":Current_Projects.objects.all(),
        "past_desc":Past_Projects_description.objects.all()[:1],
        "current_desc":Current_Projects_description.objects.all()[:1],
        "proposed_desc":Proposed_Projects_description.objects.all()[:1] 
    }
    return render(request,"portfollio.html",data)


class Proposed_Projects_detail(DetailView):
    template_name = "proposed_projects.html"
    model = Proposed_Projects

class Past_Projects_detail(DetailView):
    template_name = "past_projects.html"
    model = Past_Projects

class Current_Projects_detail(DetailView):
    template_name = "current_projects.html"
    model = Current_Projects



def blog(request):
    post_list = Blog.objects.all()
    paginator = Paginator(post_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    data = {
        'blog': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request,"blog.html",data)



def blog_details(request, pk):
    object = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        obj = Comment()
        obj.post = object
        obj.name = request.POST.get("name")
        obj.email = request.POST.get("email")
        obj.loacation = request.POST.get("location")
        obj.disc = request.POST.get("comment")
        obj.save()
        return redirect(reverse('blog-post', kwargs={'pk': object.pk}))
    return render(request,"blog_detail.html",{"object":object,"comments":Comment.objects.all(),"image_id":random.randint(1,1000)})






    
