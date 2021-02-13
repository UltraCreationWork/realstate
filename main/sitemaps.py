from django.contrib.sitemaps import Sitemap
from .models import Header,Projects,Services,Price,PrivacyPolicy,Career_header,Career
from django.urls import reverse

class Headersitemaps(Sitemap):
    
    def item(self):
        return Header.objects.all()

class Projectsitemaps(Sitemap):
    
    def item(self):
        return Projects.objects.all()
    
class Careersitemaps(Sitemap):
    
    def item(self):
        return Career.objects.all()

class Pricesitemaps(Sitemap):
    
    def item(self):
        return Price.objects.all()

class Servicessitemaps(Sitemap):
    
    def item(self):
        return Services.objects.all()

class Careerphotositemaps(Sitemap):
    
    def item(self):
        return Career_header.objects.all()


    
class Staticsitemaps(Sitemap):
    
    def item(self):
        return ['home','post','privacy','contact',"testimonial_add","career",'detail','career_detail','privacy']

    def location(self,item):
        return reverse(item)