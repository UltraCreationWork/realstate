from django.contrib.sitemaps import Sitemap
from .models import Header,Projects,Services,Price,PrivacyPolicy,Career_header,Career,Past_Projects,Current_Projects,Proposed_Projects,Blog
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

class PastProjectsitemaps(Sitemap):
    
    def items(self):
        return Past_Projects.objects.all()
    
class CurruntProjectsitemaps(Sitemap):
    
    def items(self):
        return Current_Projects.objects.all()

class ProposedProjectsitemaps(Sitemap):
    
    def items(self):
        return Proposed_Projects.objects.all()
    
class Blogsitemaps(Sitemap):
    
    def items(self):
        return Blog.objects.all()


    
class Staticsitemaps(Sitemap):
    
    def items(self):
        return ['home','privacy','contact',"testimonial_add","career"]

    def location(self,item):
        return reverse(item)