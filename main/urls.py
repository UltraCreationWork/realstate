from django.urls import path,include
from .views import (
    home,
    contact,
    header_detail_view,
    privacypolicy,
    testimonal_add,
    carrier,
    Project_detail,
    Carrier_detail,
    portfollio,
    blog,
    Proposed_Projects_detail,
    Past_Projects_detail,
    Current_Projects_detail,
    blog_details,


    )
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Headersitemaps,Staticsitemaps,Projectsitemaps,Careersitemaps,ProposedProjectsitemaps,PastProjectsitemaps,CurruntProjectsitemaps,Blogsitemaps
sitemaps = {
    'post': Headersitemaps,
    'static':Staticsitemaps,
    'projects':Projectsitemaps,
    'career':Careersitemaps,
    "past":PastProjectsitemaps,
    "current":CurruntProjectsitemaps,
    "proposed":ProposedProjectsitemaps,
    "blog":Blogsitemaps
}

urlpatterns = [
    path("",home,name="home"),
    path("portfolio/",portfollio,name="portfolio"),
    path("portfolio/past/<int:pk>",Past_Projects_detail.as_view(),name="past_projects"),
    path("blog/",blog,name="blog"),
    # path("thankyou",pass_comment,name="comment"),
    path("blog/post-detail/<int:pk>",blog_details,name="blog-post"),
    path("portfolio/current/<int:pk>",Current_Projects_detail.as_view(),name="current_projects"),
    path("portfolio/proposed/<int:pk>",Proposed_Projects_detail.as_view(),name="proposed_projects"),
    path("conatct/",contact,name="contact"),
    path("detail/<int:pk>",header_detail_view.as_view(),name="post"),
    path("privacy&policy/",privacypolicy,name="privacy"),
    path("add_testimonial/",testimonal_add,name="testimonial_add"),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps}),
    path("careers/",carrier,name="career"),
    path("project/<int:pk>",Project_detail.as_view(),name="detail"),
    path("career_detail/<int:pk>",Carrier_detail.as_view(),name="career_detail")
    
]

