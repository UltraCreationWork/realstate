from django.urls import path,include
from .views import home,contact
urlpatterns = [
    path("",home,name="home"),
    path("conatct/",contact,name="contact")
    
]

