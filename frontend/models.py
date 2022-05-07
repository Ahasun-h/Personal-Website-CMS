from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.expressions import F

from django.template.defaultfilters import default, truncatechars 
from django.conf.urls.static import static

from PIL import Image
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

from ckeditor.fields import RichTextField







# Create your models here.
class SiteSetting(models.Model):
    logo = models.ImageField(upload_to='site_image/',blank=False)
    backround_image = models.ImageField(upload_to='site_image/',blank=False)
    owner_name = models.CharField(max_length=100,blank=False)
    owner_Profession = models.CharField(max_length=200,blank=False)
    owner_moto_line = models.CharField(max_length=500,blank=False)
    symbol_image_small = models.ImageField(upload_to='site_image/',blank=False)
    symbol_image_big = models.ImageField(upload_to='site_image/',blank=False)

    
    @property
    def logo_preview(self):
        if self.logo:
            logo = get_thumbnail(self.logo,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(logo.url, logo.width, logo.height))
        return ""
    
    def __str__(self):
        return self.owner_name


class SocialMedia(models.Model):
    platform_name = models.CharField(max_length=100,blank=False)
    link = models.CharField(max_length=500,blank=False)

    def save(self, *args, **kwargs):
        self.platform_name = self.platform_name.lower()
        super(SocialMedia,self).save(*args, **kwargs)

    def __str__(self):
        return self.platform_name

class ActivePage(models.Model):
    about_page = models.BooleanField(default=True)
    resume_page = models.BooleanField(default=True)
    portfolio_page =  models.BooleanField(default=True)
    blog_page =  models.BooleanField(default=True)
    contact_page =  models.BooleanField(default=True)


        

# About Page
class AboutMe(models.Model):
    profile_image = models.ImageField(upload_to='user_image/',blank=False)
    about_content = models.TextField()
    def __str__(self):
        return self.about_content
    # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def about_description(self):
        return truncatechars(self.about_content, 20)

class Service(models.Model):
    icon = models.ImageField(upload_to='service_icon/',blank=False)
    service_name = models.CharField(max_length=1000,blank=False)
    service_detail = models.CharField(max_length=2000,blank=False)
    def __str__(self):
        return self.service_name

class WorkProcces(models.Model):
    icon = models.ImageField(upload_to='work_procces/',blank=False)
    procces_name = models.CharField(max_length=400,blank=False)
    def __str__(self):
        return self.procces_name


class WorkWith(models.Model):
    logo = models.ImageField(upload_to='clients_logo/',blank=False)
    clients_name = models.CharField(max_length=500,blank=False)
    link = models.CharField(max_length=1000,blank=False)
    def __str__(self):
        return self.clients_name


class Achivement(models.Model):
    icon = models.ImageField(upload_to='achivement_icon/',blank=False)
    detials = models.CharField(max_length=500,blank=False)
    def __str__(self):
        return self.detials
    


# Resume Page
class WorkHistory(models.Model):
    starting = models.CharField(max_length=100,blank=False)
    ending = models.CharField(max_length=100,blank=False)
    designation = models.CharField(max_length=500,blank=False)
    company_name = models.CharField(max_length=500,blank=False)
    content = models.TextField()
    def __str__(self):
        return self.company_name
     # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def work_history_description(self):
        return truncatechars(self.content, 20)
    


class Education(models.Model):
    starting = models.CharField(max_length=100,blank=False)
    ending = models.CharField(max_length=100,blank=True)
    subject = models.CharField(max_length=500,blank=False)
    institute_name = models.CharField(max_length=500,blank=False)
    content = models.TextField()
    def __str__(self):
        return self.institute_name
    @property
    def education_description(self):
        return truncatechars(self.content, 20)

class Skill(models.Model):
    platform_name = models.CharField(max_length=400,blank=True)
    skill_percentage = models.IntegerField(blank=False)
    def __str__(self):
        return self.platform_name
    

class Testimonial(models.Model):
    clients_name = models.CharField(max_length=500,blank=False)
    clients_designation = models.CharField(max_length=500,blank=True)
    clients_image = models.ImageField(upload_to='cilents_image/',blank=True)
    company_name = models.CharField(max_length=500,blank=True)
    detials = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.clients_image.path)

        if img.height > 150 or img.weight >150 :
            output_size = (150,150 )
            img.thumbnail(output_size)
            img.save(self.clients_image.path)
    @property
    def testimonial_description(self):
        return truncatechars(self.detials, 20)

# Contact Page
class ContatInformation(models.Model):
    icon = models.ImageField(upload_to='contact_icon/',blank=False)
    details = models.CharField(max_length=400,blank=False)
    def __str__(self):
        return self.details



# Portfolio Page
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=200,blank=False,unique=True)
    category_class = models.CharField(max_length=200,blank=False,unique=True)

    def save(self, *args, **kwargs):
        self.category_class = self.category_class.lower()
        self.name = self.name.upper()
        super(PortfolioCategory,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    project_name = models.CharField(max_length=300,blank=False)
    category_class = models.ForeignKey(PortfolioCategory,on_delete=models.PROTECT,default = 1,verbose_name="Category")
    image = models.ImageField(upload_to='portfolio_item/',blank=False)
    link = models.CharField(max_length=400,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 400 or img.weight > 600 :
            output_size = (600,400 )
            img.thumbnail(output_size)
            img.save(self.image.path)
    def __str__(self):
        return self.project_name



# Email Setting

class EmailSetting(models.Model):
    email_host = models.CharField(max_length=200,blank=False)
    email_port = models.IntegerField(blank=False)
    user_email = models.EmailField(max_length=200,blank=False)
    password = models.CharField(max_length=10,blank=False)
    email_tls = models.BooleanField(blank=False)

class EmailSettingAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        form_instance.fields['email_host'].widget.attrs['placeholder'] = 'smtp.gmail.com'
        form_instance.fields['email_port'].widget.attrs['placeholder'] = '587'
        return super().render_change_form(request, context, *args, **kwargs)

def __str__(self):
        return self.email

# Blog Category
class BlogCategory(models.Model):
    post_category_name = models.CharField(max_length=20,blank=False)
    publish_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.post_category_name
    

# BLog 
class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    post_image = models.ImageField(upload_to='post_image/',blank=False)
    slug = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_ctegory = models.ForeignKey(BlogCategory,related_name='post_category', on_delete=models.CASCADE,default=1)
    intro = models.TextField(max_length=255,default='Reade More...')
    body = RichTextField(blank=False,null=True)
    post_date = models.DateField(auto_now_add=True)
   
    class Meta:
        ordering = ['post_date']

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    replay = models.TextField(blank=True)

    class Meta:
        ordering = ['date_added']

# Coustom Code
class CustomCS(models.Model):
    code = models.TextField(blank=False)
    active = models.BooleanField(default=True)
    publish_date = models.DateField(auto_now_add=True)

class CustomScript(models.Model):
    code = models.TextField(blank=False)
    active = models.BooleanField(default=True)
    publish_date = models.DateField(auto_now_add=True)

# Social media Chat Button  
class ChatButton(models.Model):
    name = models.CharField(max_length=200,blank=False)
    code = models.TextField(blank=False)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.code)


# setting
class Setting(models.Model):
    description = models.CharField(max_length=200,blank=False)
    author = models.CharField(max_length=200,blank=False)
    keywords = models.TextField(blank=False)
    Website_title = models.CharField(max_length=20,blank=False)
    favicon = models.ImageField(upload_to='site_image/',blank=False)
    copyright = models.CharField(max_length=200,blank=False)


class CurriculumVitae(models.Model):
    publish_date = models.DateField(auto_now_add=True)
    cv = models.FileField(upload_to='uploaded_cv/',blank=False)





       





        




        
    
    

    
    

    



    

