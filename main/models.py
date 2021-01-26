from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse


Icon = (
    ("ri-adjust","ri-adjust"),
    ("ri-arrow-down","ri-arrow-down"),
    ("ri-arrow-left","ri-arrow-left"),
    ("ri-arrow-right","ri-arrow-right"),
    ("ri-arrow-up","ri-arrow-up"),
    ("ri-bookmark","ri-bookmark"),
    ("ri-bucket","ri-bucket"),
    ("ri-bullhorn","ri-bullhorn"),
    ("ri-calendar","ri-calendar"),
    ("ri-check-square","ri-check-square"),
    ("ri-check","ri-check"),
    ("ri-chevron-down","ri-chevron-down"),
    ("ri-chevron-down-circle","ri-chevron-down-circle"),
    ("ri-chevron-left-circle","ri-chevron-left-circle"),
    ("ri-chevron-left","ri-chevron-left"),
    ("ri-chevron-right-circle","ri-chevron-right-circle"),
    ("ri-chevron-right-circle","ri-chevron-right-circle"),
    ("ri-chevron-right","ri-chevron-right"),
    ("ri-chevron-top-circle","ri-chevron-top-circle"),
    ("ri-chevron-up","ri-chevron-up"),
    ("ri-clock","ri-clock"),
    ("ri-cloud-download","ri-cloud-download"),
    ("ri-cloud-upload","ri-cloud-upload"),
    ("ri-cloud","ri-cloud"),
    ("ri-comment-bubble","ri-comment-bubble"),
    ("ri-comment-square","ri-comment-square"),
    ("ri-comment-txt-square","ri-comment-txt-square"),
    ("ri-comments-bubble","ri-comments-bubble"),
    ("ri-computer","ri-computer"),
    ("ri-contract","ri-contract"),
    ("ri-crop","ri-crop"),
    ("ri-cross-circle","ri-cross-circle"),
    ("ri-cross","ri-cross"),
    ("ri-cutlery","ri-cutlery"),
    ("ri-diamond","ri-diamond"),
    ("ri-document-add","ri-document-add"),
    ("ri-document-remove","ri-document-remove"),
    ("ri-document","ri-document"),
    ("ri-download","ri-download"),
    ("ri-dribbble","ri-dribbble"),
    ("ri-drop","ri-drop"),
    ("ri-earth","ri-earth"),
    ("ri-envelope","ri-envelope"),
    ("ri-equal-circle","ri-equal-circle"),
    ("ri-exclamation-circle","ri-exclamation-circle"),
    ("ri-exclamation-triangle","ri-exclamation-triangle"),
    ("ri-expand","ri-expand"),
    ("ri-eye-close","ri-eye-close"),
    ("ri-eye","ri-eye"),
    ("ri-facebook","ri-facebook"),
    ("ri-film-play","ri-film-play"),
    ("ri-flag","ri-flag"),
    ("ri-glasses-classic","ri-glasses-classic"),
    ("ri-glasses-hipster","ri-glasses-hipster"),
    ("ri-google-plus","ri-google-plus"),
    ("ri-google","ri-google"),
    ("ri-hamburger-circle","ri-hamburger-circle"),
    ("ri-hamburger","ri-hamburger"),
    ("ri-heart","ri-heart"),
    ("ri-history","ri-history"),
    ("ri-home","ri-home"),
    ("ri-info-circle","ri-info-circle"),
    ("ri-laptop","ri-laptop"),
    ("ri-leaf","ri-leaf"),
    ("ri-link","ri-link"),
    ("ri-list","ri-list"),
    ("ri-location","ri-location"),
    ("ri-lock","ri-lock"),
    ("ri-map-marker","ri-map-marker"),
    ("ri-map","ri-map"),
    ("ri-meh","ri-meh"),
    ("ri-microphone","ri-microphone"),
    ("ri-minus-circle","ri-minus-circle"),
    ("ri-moon","ri-moon"),
    ("ri-move","ri-move"),
    ("ri-music-note-double","ri-music-note-double"),
    ("ri-music-note","ri-music-note"),
    ("ri-mustache","ri-mustache"),
    ("ri-ok-circle","ri-ok-circle"),
    ("ri-paperclip","ri-paperclip"),
    ("ri-pencil-square","ri-pencil-square"),
    ("ri-pencil","ri-pencil"),
    ("ri-plus-circle","ri-plus-circle"),
    ("ri-power-switch","ri-power-switch"),
    ("ri-pushpin","ri-pushpin"),
    ("ri-question-circle","ri-question-circle"),
    ("ri-random","ri-random"),
    ("ri-redo","ri-redo"),
    ("ri-refresh","ri-refresh"),
    ("ri-resize-full","ri-resize-full"),
    ("ri-resize-h","ri-resize-h"),
    ("ri-resize-small","ri-resize-small"),
    ("ri-resize-v","ri-resize-v"),
    ("ri-retweet","ri-retweet"),
    ("ri-rivoli","ri-rivoli"),
    ("ri-sad","ri-sad"),
    ("ri-search-minus","ri-search-minus"),
    ("ri-search-plus","ri-search-plus"),
    ("ri-search","ri-search"),
    ("ri-share-square","ri-share-square"),
    ("ri-share","ri-share"),
    ("ri-shopping-cart","ri-shopping-cart"),
    ("ri-smile","ri-smile"),
    ("ri-star-half-empty","ri-star-half-empty"),
    ("ri-star","ri-star"),
    ("ri-stats","ri-stats"),
    ("ri-sun","ri-sun"),
    ("ri-tag","ri-tag"),
    ("ri-th-large","ri-th-large"),
    ("ri-th-large","ri-th-large"),
    ("ri-th-list","ri-th-list"),
    ("ri-th","ri-th"),
    ("ri-thumbs-down","ri-thumbs-down"),
    ("ri-thumbs-up","ri-thumbs-up"),
    ("ri-trash","ri-trash"),
    ("ri-tumblr","ri-tumblr"),
    ("ri-twitter","ri-twitter"),
    ("ri-undo","ri-undo"),
    ("ri-unlink","ri-unlink"),
    ("ri-unlock","ri-unlock"),
    ("ri-upload","ri-upload"),
    ("ri-user-girl","ri-user-girl"),
    ("ri-user","ri-user"),
    ("ri-users","ri-users"),
    ("ri-volume-level-one","ri-volume-level-one"),
    ("ri-volume-level-three","ri-volume-level-three"),
    ("ri-volume-level-two","ri-volume-level-two"),
    ("ri-volume","ri-volume"),
    ("ri-wrench","ri-wrench"),
    ("ri-youtube-play","ri-youtube-play"),
    ("ri-youtube","ri-youtube")
)
class Artitecture(models.Model):
    name = models.CharField(max_length=15,verbose_name="Architecture Name")
    img = models.ImageField(upload_to="realestate/architecture",verbose_name="Image")
    about_me = RichTextField(verbose_name="About Me")
    social_link_1 = models.URLField(verbose_name="Twitter link",blank=True)
    social_link_2 = models.URLField(verbose_name="Facebook Link",blank=True)
    social_link_3 = models.URLField(verbose_name="Instagram link",blank=True)
    social_link_4 = models.URLField(verbose_name="Linkedin link",blank=True)
    number = models.IntegerField(verbose_name="Serical Number")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["number"]

class website_title(models.Model):
    number = models.IntegerField(verbose_name="Number")
    title  = models.CharField(max_length=100,verbose_name="Title")
    content = models.CharField(max_length=100,verbose_name="SEO Content")
    keywords = models.CharField(max_length=100,verbose_name="SEO Keyword Comma Seperated")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-number"]


class Header(models.Model):
    header_img = models.ImageField(upload_to="realestate/header",verbose_name="Header Image")
    additional_img_1 = models.ImageField(upload_to="realestate/property",verbose_name="Side image")
    additional_img_2 = models.ImageField(upload_to="realestate/property",verbose_name="Side image")
    property_video = models.CharField(max_length=2000,verbose_name="Iframe of your property video")
    title = models.CharField(max_length=60,verbose_name="Title")
    content = models.CharField(max_length=200,verbose_name="Content Box")
    about_this = RichTextField(verbose_name="About This Project")
    loacation = models.CharField(max_length=2000,verbose_name="Google location of Property")
    number = models.IntegerField(verbose_name="Serial Number")


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post",kwargs={"pk":self.pk})

    class Meta:
        ordering = ["number"]


class Aboutus(models.Model):
    number = models.IntegerField(verbose_name="serial Number")
    img_1 = models.ImageField(upload_to="realestate/aboutus",verbose_name="About Header Image")
    img_2 = models.ImageField(upload_to="realestate/aboutus",verbose_name="Image")
    paragraph = models.CharField(max_length=100,verbose_name="Main Paragrph")
    point_1 = models.CharField(max_length=50,verbose_name="Point one")
    point_2 = models.CharField(max_length=50,verbose_name="Point two")
    point_3 = models.CharField(max_length=50,verbose_name="Point three")
    content = RichTextField(verbose_name="About Us Content Box")

    def __number__(self):
        return self.number
    class Meta:
        ordering = ["-number"]


class Feature(models.Model):
    number = models.IntegerField(verbose_name="Featur Serial Number")
    icon = models.CharField(max_length=23,choices=Icon)
    title = models.CharField(max_length=100,verbose_name="Feature Name")
    img = models.ImageField(upload_to="realestate/feature",verbose_name="Image of Work")
    paragraph = RichTextField(verbose_name="Feature Discription")
    point_1 = models.CharField(max_length=50,verbose_name="Point one",blank=True)
    point_2 = models.CharField(max_length=50,verbose_name="Point two",blank=True)
    point_3 = models.CharField(max_length=50,verbose_name="Point three",blank=True)
    point_4 = models.CharField(max_length=50,verbose_name="Point Four",blank=True)
    point_5 = models.CharField(max_length=50,verbose_name="Point Five",blank=True)
    point_6 = models.CharField(max_length=50,verbose_name="Point Six",blank=True)
    point_7 = models.CharField(max_length=50,verbose_name="Point Seven",blank=True)
    point_8 = models.CharField(max_length=50,verbose_name="Point Eight",blank=True)
    point_9 = models.CharField(max_length=50,verbose_name="Point Nine",blank=True)
    point_10 = models.CharField(max_length=50,verbose_name="Point Ten",blank=True)
    point_11 = models.CharField(max_length=50,verbose_name="Point Eleven",blank=True)
    point_12 = models.CharField(max_length=50,verbose_name="Point Twele",blank=True)
    point_13 = models.CharField(max_length=50,verbose_name="Point Thirteen",blank=True)
    point_14 = models.CharField(max_length=50,verbose_name="Point Fourteen",blank=True)
    point_15 = models.CharField(max_length=50,verbose_name="Point Fifteen",blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["number"]



    

class Testimonial(models.Model):
    name                =       models.CharField(max_length=255,verbose_name="Name")
    prop_img            =       models.ImageField(upload_to='realestate/testimonial',verbose_name="Project Image")
    img                 =       models.ImageField(upload_to='realestate/testimonial',verbose_name="Image")
    prof                =       models.CharField(max_length=100,verbose_name="Profession")
    disc                =       models.CharField(max_length=500,verbose_name="Review")
    social_link_f       =       models.URLField(default="facebook.com",blank=True)
    social_link_t       =       models.URLField(default="twiter.com",blank=True)
    social_link_i       =       models.URLField(default="instagram.com",blank=True)
    social_link_l       =       models.URLField(default="linkedin.com",blank=True)

    def __str__(self):
        return self.name

class Services(models.Model):
    symbol = models.CharField(max_length=255 ,blank=True,verbose_name="Synbol")
    name = models.CharField(max_length=500,verbose_name="Name")
    dics = RichTextField(verbose_name="Content")
    number = models.IntegerField(verbose_name="Number")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['number']

class Projects(models.Model):
    photo           =       models.ImageField(upload_to='realestate/projects') 
    field           =       models.CharField(max_length=255,verbose_name="Title")
    date            =       models.DateField(verbose_name="Project Done Date")
    number          =       models.IntegerField(verbose_name="Serial Number")

    def __str__(self):
        return self.field
    
    class Meta:
        ordering = ['-number']





class Price(models.Model):
    number = models.IntegerField(verbose_name=" Serial Number")
    title = models.CharField(max_length=10,verbose_name="Package Name")
    service_1 = models.CharField(max_length=20,verbose_name="Service",blank=True)
    service_2 = models.CharField(max_length=20,verbose_name="Service number two",blank=True)
    service_3 = models.CharField(max_length=20,verbose_name="Service number three",blank=True)
    service_4 = models.CharField(max_length=20,verbose_name="Service number four",blank=True)
    service_5 = models.CharField(max_length=20,verbose_name="Service number five",blank=True)
    buy_now_link = models.URLField(verbose_name="Buy Now Link")

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-number"]

class FAQ(models.Model):
    number = models.IntegerField(verbose_name="Question Number")
    question = models.CharField(max_length=50,verbose_name="Question")
    answer = RichTextField(verbose_name="Answer of this question")

    def __number__(self):
        return self.number
    class Meta:
        ordering = ["number"]



class Contact(models.Model):
    name = models.CharField(max_length=255,verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=500,verbose_name="Subject")
    message = models.TextField(verbose_name="Messsage")
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name="Time")
    
    def __str__(self):
        return self.name

class PrivancyPolicy(models.Model):
    number = models.IntegerField(verbose_name="Serial Number")
    title = models.CharField(max_length=20,verbose_name="Title")
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-number"]





class Footer(models.Model):
    title = models.CharField(max_length=10,verbose_name="Company Name")
    paragraph = models.CharField(max_length=50,verbose_name="Content Box")
    link_1 = models.URLField(verbose_name="Twitter link")
    link_2 = models.URLField(verbose_name="Facebook link")
    link_3 = models.URLField(verbose_name="Instagram link")
    link_4 = models.URLField(verbose_name="Linkedin link")
    serial_number = models.IntegerField(verbose_name="Serial Number")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-serial_number"]

class Contact_Detail(models.Model):
    number = models.IntegerField(verbose_name="Serial Number")
    content = RichTextField(verbose_name="Why Contact Us")
    location = models.CharField(max_length=2000,verbose_name="google location")
    address = models.CharField(max_length=20,verbose_name="Address")
    country = models.CharField(max_length=10,default="India",verbose_name="Country")
    email = models.EmailField(verbose_name="Email Address")
    phone = PhoneNumberField(verbose_name="Phone Number")
    tollfree = models.CharField(max_length=13,verbose_name="Toll Free Number")
    social_link_1 = models.URLField(verbose_name="Twitter link",blank=True)
    social_link_2 = models.URLField(verbose_name="Facebook Link",blank=True)
    social_link_3 = models.URLField(verbose_name="Instagram link",blank=True)
    social_link_4 = models.URLField(verbose_name="Linkedin link",blank=True)

    def __number__(self):
        return self.number

    class Meta:
        ordering = ["-number"]



