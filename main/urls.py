from django.urls import path,include
from .views import home,contact,header_detail_view,privacypolicy,testimonal_add,carrier,Project_detail,Carrier_detail
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Postsitemaps,Staticsitemaps
sitemaps = {
    'post': Postsitemaps,
    'static':Staticsitemaps
}
urlpatterns = [
    path("",home,name="home"),
    path("conatct/",contact,name="contact"),
    path("detail/<int:pk>",header_detail_view.as_view(),name="post"),
    path("privacy&policy/",privacypolicy,name="privacy"),
    path("add_testimonial/",testimonal_add,name="testimonial_add"),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps}),
    path("careers/",carrier,name="career"),
    path("project/<int:pk>",Project_detail.as_view(),name="detail"),
    path("career_detail/<int:pk>",Carrier_detail.as_view(),name="career_detail")
    
]

