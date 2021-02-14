from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse

catagory = (
    ("Commercial","Commercial"),
    ("Residential","Residential"),
    ("Clinic/Hospital","Clinic/Hospital"),
    ("Institutional","Institutional"),
    ("Interior","Interior"),
    ("Architecture","Architecture")
)

class Artitecture(models.Model):
    name = models.CharField(max_length=15,verbose_name="Architecture Name")
    img = models.ImageField(upload_to="realestate/architecture",verbose_name="Image")
    about_me = RichTextField(verbose_name="About Me")
    social_link_1 = models.URLField(verbose_name="Twitter link",blank=True)
    social_link_2 = models.URLField(verbose_name="Facebook Link",blank=True)
    social_link_3 = models.URLField(verbose_name="Instagram link",blank=True)
    social_link_4 = models.URLField(verbose_name="Linkedin link",blank=True)
    number = models.PositiveIntegerField(verbose_name="Serical Number")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["number"]

class website_title(models.Model):
    number = models.PositiveIntegerField(verbose_name="Number")
    title  = models.CharField(max_length=100,verbose_name="Title")
    content = models.CharField(max_length=100,verbose_name="SEO Content")
    keywords = models.CharField(max_length=100,verbose_name="SEO Keyword Comma Seperated")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-number"]

choise = (
    ("For Sale","For Sale"),
    ("For Rent","For Rent"),
    ("For Design","For Design")
)
class Header(models.Model):
    property_id = models.CharField(verbose_name="Poperty Id",max_length=16)
    property_type = models.CharField(verbose_name="Type Of Property",max_length=20)
    status = models.CharField(choices=choise,verbose_name="Perpose",max_length=10,blank=True)
    address = models.CharField(verbose_name="Address",max_length=100,blank=True)
    header_img = models.ImageField(upload_to="realestate/header",verbose_name="Header Image")
    additional_img_1 = models.ImageField(upload_to="realestate/property",verbose_name="Side image",blank=True)
    additional_img_2 = models.ImageField(upload_to="realestate/property",verbose_name="Side image",blank=True)
    property_video = models.CharField(max_length=2000,verbose_name="Iframe of your property video",blank=True)
    title = models.CharField(max_length=60,verbose_name="Title")
    content = models.CharField(max_length=200,verbose_name="Content Box",blank=True)
    about_this = RichTextField(verbose_name="About This Project")
    loacation = models.CharField(max_length=2000,verbose_name="Google location of Property",blank=True)
    number = models.PositiveIntegerField(verbose_name="Serial Number")
    price = models.PositiveIntegerField(verbose_name="Price",blank=True)
    area  = models.PositiveIntegerField(verbose_name="Area In Squre Ft.",blank=True)
    hall = models.PositiveIntegerField(verbose_name="Number of Hall",blank=True)
    beds = models.PositiveIntegerField(verbose_name="Number of Bedroom",blank=True)
    bath = models.PositiveIntegerField(verbose_name="Nomber of Baths",blank=True)
    






    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post",kwargs={"pk":self.pk})

    class Meta:
        ordering = ["number"]


class Aboutus(models.Model):
    number = models.PositiveIntegerField(verbose_name="serial Number")
    img_1 = models.ImageField(upload_to="realestate/aboutus",verbose_name="About Header Image")
    img_2 = models.ImageField(upload_to="realestate/aboutus",verbose_name="Image")
    paragraph = models.CharField(max_length=100,verbose_name="Main Paragrph",blank=True)
    point_1 = models.CharField(max_length=50,verbose_name="Point one",blank=True)
    point_2 = models.CharField(max_length=50,verbose_name="Point two",blank=True)
    point_3 = models.CharField(max_length=50,verbose_name="Point three",blank=True)
    content = RichTextField(verbose_name="About Us Content Box")

    def __number__(self):
        return self.number
    class Meta:
        ordering = ["-number"]


class Feature(models.Model):
    number = models.PositiveIntegerField(verbose_name="Featur Serial Number")
    icon = models.CharField(max_length=23,verbose_name="Icon")
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
    prof                =       models.CharField(max_length=100,verbose_name="Profession",blank=True)
    disc                =       models.CharField(max_length=500,verbose_name="Review")
    social_link_f       =       models.URLField(default="facebook.com",blank=True)
    social_link_t       =       models.URLField(default="twiter.com",blank=True)
    social_link_i       =       models.URLField(default="instagram.com",blank=True)
    social_link_l       =       models.URLField(default="linkedin.com",blank=True)

    def __str__(self):
        return self.name

class Services(models.Model):
    symbol = models.CharField(max_length=255,blank=True,verbose_name="Icon")
    name = models.CharField(max_length=500,verbose_name="Name")
    dics = RichTextField(verbose_name="Content")
    number = models.PositiveIntegerField(verbose_name="Number")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['number']

class Projects(models.Model):
    photo           =       models.ImageField(upload_to='realestate/projects') 
    field           =       models.CharField(max_length=255,verbose_name="Title")
    content         =       RichTextField(verbose_name="Content")
    date            =       models.DateField(verbose_name="Project Done Date")
    number          =       models.PositiveIntegerField(verbose_name="Serial Number")

    def __str__(self):
        return self.field
    
    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk":self.pk})
    
    class Meta:
        ordering = ['-number']





class Price(models.Model):
    number = models.PositiveIntegerField(verbose_name=" Serial Number")
    price = models.PositiveIntegerField(verbose_name="service charge")
    parameter = models.CharField(max_length=10,verbose_name="basis of parameter like (month,squre ft,squre meeter etc.)")
    title = models.CharField(max_length=50,verbose_name="Package Name")
    service_1 = models.CharField(max_length=100,verbose_name="Service",blank=True)
    service_2 = models.CharField(max_length=100,verbose_name="Service number two",blank=True)
    service_3 = models.CharField(max_length=100,verbose_name="Service number three",blank=True)
    service_4 = models.CharField(max_length=100,verbose_name="Service number four",blank=True)
    service_5 = models.CharField(max_length=100,verbose_name="Service number five",blank=True)
    service_6 = models.CharField(max_length=100,verbose_name="Service",blank=True)
    service_7 = models.CharField(max_length=100,verbose_name="Service number two",blank=True)
    service_8 = models.CharField(max_length=100,verbose_name="Service number three",blank=True)
    service_9 = models.CharField(max_length=100,verbose_name="Service number four",blank=True)
    service_10 = models.CharField(max_length=100,verbose_name="Service number five",blank=True)
    buy_now_link = models.URLField(verbose_name="Buy Now Link",blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-number"]

class FAQ(models.Model):
    number = models.PositiveIntegerField(verbose_name="Question Number")
    question = models.CharField(max_length=50,verbose_name="Question")
    answer = RichTextField(verbose_name="Answer of this question")

    def __number__(self):
        return self.number
    class Meta:
        ordering = ["number"]



class Contact(models.Model):
    name = models.CharField(max_length=255,verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    mobile_no = PhoneNumberField(verbose_name="Phone Number",blank=True)
    subject = models.CharField(max_length=500,verbose_name="Subject",blank=True)
    message = models.TextField(verbose_name="Messsage")
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name="Time")
    
    def __str__(self):
        return self.name

class PrivacyPolicy(models.Model):
    number = models.PositiveIntegerField(verbose_name="Serial Number")
    title = models.CharField(max_length=20,verbose_name="Title")
    content = RichTextField(verbose_name="Content")

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
    serial_number = models.PositiveIntegerField(verbose_name="Serial Number")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-serial_number"]

class Contact_Detail(models.Model):
    number = models.PositiveIntegerField(verbose_name="Serial Number")
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


class Career_header(models.Model):
    title = models.CharField(max_length=50,verbose_name="image tittle")
    img = models.ImageField(verbose_name="Image For Career Page")
    date = models.DateField(auto_now_add=True)
    number = models.IntegerField(verbose_name="Serial Number")

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-number"]



class Career(models.Model):
    number = models.PositiveIntegerField(verbose_name="Featur Serial Number")
    icon = models.CharField(max_length=23,verbose_name="Icon")
    title = models.CharField(max_length=100,verbose_name="Post Name")
    img = models.ImageField(upload_to="realestate/feature",verbose_name="Image of Work")
    paragraph = RichTextField(verbose_name="Post Discription")
    point_1 = models.CharField(max_length=200,verbose_name="heading",blank=True)
    point_2 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_3 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_4 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_5 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_6 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_7 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_8 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_9 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_10 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_11 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_12 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_13 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_14 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    point_15 = models.CharField(max_length=200,verbose_name="Requrements",blank=True)
    url = models.URLField(verbose_name="application url",blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("career_detail",kwargs={"pk":self.pk})
    
    class Meta:
        ordering = ["number"]


class Proposed_Projects(models.Model):
    project_number  = models.PositiveIntegerField(verbose_name="Serial Number")
    filter_by       = models.CharField(choices=catagory,max_length=100,verbose_name="filter By")
    project_title   = models.CharField(max_length=100,verbose_name="Title",blank=True)
    clint_name      = models.CharField(max_length=200,verbose_name="Name",blank=True)
    loc             = models.CharField(max_length=500,verbose_name="Address of this Project",blank=True)
    main_image      = models.ImageField(upload_to="projects/proposed_projects",verbose_name="main Image")
    second_image    = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Second Image")
    third_image     = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Third Image")
    fouth_image     = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Fourth Image")
    disc            = RichTextField(verbose_name="Description")
    date            = models.DateField(verbose_name="Date")

    def __str__(self):
        return self.project_title
    
    def get_absolute_url(self):
        return reverse("proposed_projects",kwargs={"pk":self.pk})

    class Meta:
        ordering = ["project_number"]

class Past_Projects(models.Model):
    project_number  = models.PositiveIntegerField(verbose_name="Serial Number")
    filter_by       = models.CharField(choices=catagory,max_length=100,verbose_name="filter By")
    project_title   = models.CharField(max_length=100,verbose_name="Title",blank=True)
    clint_name      = models.CharField(max_length=200,verbose_name="Name",blank=True)
    loc             = models.CharField(max_length=500,verbose_name="Address of this Project",blank=True)
    main_image      = models.ImageField(upload_to="projects/proposed_projects",verbose_name="main Image")
    second_image    = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Second Image")
    third_image     = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Third Image")
    fouth_image     = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Fourth Image")
    disc            = RichTextField(verbose_name="Description")
    date            = models.DateField(verbose_name="Date")

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse("past_projects",kwargs={"pk":self.pk})

    class Meta:
        ordering = ["project_number"]


class Current_Projects(models.Model):
    project_number  = models.PositiveIntegerField(verbose_name="Serial Number")
    filter_by       = models.CharField(choices=catagory,max_length=100,verbose_name="filter By")
    project_title   = models.CharField(max_length=100,verbose_name="Title",blank=True)
    clint_name      = models.CharField(max_length=200,verbose_name="Name",blank=True)
    loc             = models.CharField(max_length=500,verbose_name="Address of this Project",blank=True)
    main_image      = models.ImageField(upload_to="projects/proposed_projects",verbose_name="main Image")
    second_image    = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Second Image")
    third_image     = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Third Image")
    fouth_image     = models.ImageField(upload_to="projects/proposed_projects",verbose_name="Fourth Image")
    disc            = RichTextField(verbose_name="Description")
    date            = models.DateField(verbose_name="Date")

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse("current_projects",kwargs={"pk":self.pk})
        
    class Meta:
        ordering = ["project_number"]




class Blog(models.Model):
    title       = models.CharField(max_length=100,verbose_name="title")
    blog_image  = models.ImageField(upload_to="blog_photos/",verbose_name="Post Image")
    overview    = models.CharField(max_length=300,verbose_name="overview")
    disc        = RichTextField()
    catagory    = models.CharField(choices=catagory,max_length=200,verbose_name="Category")
    date        = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-post",kwargs={"pk":self.pk})

    
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-date')

    class Meta:
        ordering = ["-date"]

class Comment(models.Model):
    post = models.ForeignKey("Blog",on_delete=models.CASCADE)
    name = models.CharField(max_length=200,verbose_name="name")
    email = models.EmailField(verbose_name="email")
    loacation = models.CharField(max_length=300,verbose_name="location",blank=True)
    disc = RichTextField(verbose_name="Description")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Proposed_Projects_description(models.Model):
    serial_no = models.PositiveIntegerField(verbose_name="Serial Number")
    content = RichTextField(verbose_name="Description")

    class Meta:
        ordering = ['-serial_no']
    
class Past_Projects_description(models.Model):
    serial_no = models.PositiveIntegerField(verbose_name="Serial Number")
    content = RichTextField(verbose_name="Description")

    class Meta:
        ordering = ['-serial_no']
    
class Current_Projects_description(models.Model):
    serial_no = models.PositiveIntegerField(verbose_name="Serial Number")
    content = RichTextField(verbose_name="Description")

    class Meta:
        ordering = ['-serial_no']
    
    
    


    
    
    
    

    
    
    
    
    
    
        






