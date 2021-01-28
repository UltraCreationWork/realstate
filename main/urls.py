from django.urls import path,include
from .views import home,contact,header_detail_view,privacypolicy
urlpatterns = [
    path("",home,name="home"),
    path("conatct/",contact,name="contact"),
    path("detail/<int:pk>",header_detail_view.as_view(),name="post"),
    path("privacy&policy/",privacypolicy,name="privacy")
    
]

