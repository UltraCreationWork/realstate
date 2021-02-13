from django.contrib.sitemaps import Sitemap
from .models import Header,Projects,Services,Price,PrivacyPolicy,Career_header,Career
from django.urls import reverse

class Headersitemaps(Sitemap):
    
    def items(self):
        return Header.objects.all()

class Projectsitemaps(Sitemap):
    
    def items(self):
        return Projects.objects.all()
    
class Careersitemaps(Sitemap):
    
    def items(self):
        return Career.objects.all()

class Pricesitemaps(Sitemap):
    
    def items(self):
        return Price.objects.all()

class Servicessitemaps(Sitemap):
    
    def items(self):
        return Services.objects.all()

class Careerphotositemaps(Sitemap):
    
    def items(self):
        return Career_header.objects.all()


    
class Staticsitemaps(Sitemap):
    
    def items(self):
        return ['home','privacy','contact',"testimonial_add","career"]

    def location(self,item):
        return reverse(item)