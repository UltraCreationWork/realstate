from django.contrib.sitemaps import Sitemap
from .models import Header
from django.urls import reverse

class Postsitemaps(Sitemap):
    
    def post(self):
        return Header.objects.all()
    
class Staticsitemaps(Sitemap):
    
    def item(self):
        return ['home','post','privacy','contact',"testimonial_add"]

    def location(self,item):
        return reverse(item)