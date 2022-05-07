from django.core import paginator
from django.shortcuts import render,redirect
from .models import SiteSetting
from .models import SocialMedia
from .models import ActivePage

# About Page
from .models import AboutMe
from .models import Service
from .models import WorkProcces
from .models import WorkWith
from .models import Achivement

# Resume Page
from .models import WorkHistory
from .models import Education
from .models import Skill
from .models import Testimonial
from .models import CurriculumVitae

# Portfolio Page
from .models import PortfolioCategory
from .models import PortfolioItem

#Contact Page
from .models import ContatInformation
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# BlogPost
from .models import BlogPost
from .forms import CommentForm
from django.core.paginator import Paginator,EmptyPage


# setting
from .models import Setting

# Coustom Code
from .models import CustomCS
from .models import CustomScript

# Social media Chat Button
from .models import ChatButton 

from django.conf import settings

from html import unescape


# Create your views here.

def index(request):
    siteSettingData = SiteSetting.objects.all().last()
    socilMeadiLinksData = SocialMedia.objects.all()
    activePageData = ActivePage.objects.all().last()

    setting = Setting.objects.all().last()
    customCSS = CustomCS.objects.all()
    customScript = CustomScript.objects.all()
    chatButton = ChatButton.objects.all().last()
    
    context = {
        'siteSetting' : siteSettingData,
        'socilMeadiLinks' : socilMeadiLinksData,
        'activePage' : activePageData,
        'Setting' : setting,
        'CustomCode' : customCSS,
        'CustomScript' : customScript,
        'ChatButton' : chatButton,
    }
    return render(request,'page/index.html',context)

# About Page
def about(request):
    aboutMeData = AboutMe.objects.all().last()
    serviceData = Service.objects.all()
    workProccesData = WorkProcces.objects.all()
    workWithData = WorkWith.objects.all()
    achivementData = Achivement.objects.all()

    setting = Setting.objects.all().last()
    customCSS = CustomCS.objects.all()
    customScript = CustomScript.objects.all()
    chatButton = ChatButton.objects.all().last()

    context = {
        'AboutMe' : aboutMeData,
        'Service' : serviceData,
        'WorkProcces' : workProccesData,
        'WorkWith' : workWithData,
        'Achivement' : achivementData,
        'Setting' : setting,
        'CustomCode' : customCSS,
        'CustomScript' : customScript,
        'ChatButton' : chatButton,
    }
    return render(request,'page/about.html',context)

# resume
def resume (request):
    workHistoryData = WorkHistory.objects.all()
    educationData = Education.objects.all()
    skillData = Skill.objects.all()
    testimonialData = Testimonial.objects.all()
    curriculumVitae = CurriculumVitae.objects.all().last()
    
    setting = Setting.objects.all().last()
    customCSS = CustomCS.objects.all()
    customScript = CustomScript.objects.all()
    chatButton = ChatButton.objects.all().last()
    context = {
        'WorkHistory' : workHistoryData,
        'Education' : educationData,
        'Skill' : skillData,
        'Testimonial' : testimonialData,
        'CurriculumVitae' : curriculumVitae,
        'Setting' : setting,
        'CustomCode' : customCSS,
        'CustomScript' : customScript,
        'ChatButton' : chatButton,
    }
    return render(request,'page/resume.html',context)

# Portfolio Page
def portfolio (request):
    portfolioCategoryData = PortfolioCategory.objects.all()
    portfolioItemData = PortfolioItem.objects.all()
    
    setting = Setting.objects.all().last()
    customCSS = CustomCS.objects.all()
    customScript = CustomScript.objects.all()
    chatButton = ChatButton.objects.all().last()
    context = {
        'PortfolioCategory' : portfolioCategoryData,
        'PortfolioItem' : portfolioItemData,
        'Setting' : setting,
        'CustomCode' : customCSS,
        'CustomScript' : customScript,
        'ChatButton' : chatButton,
    }
    return render(request,'page/portfolio.html',context)



 


# Contact Page
def contact (request):
    contatInformationData =  ContatInformation.objects.all();
    
    setting = Setting.objects.all().last()
    customCSS = CustomCS.objects.all()
    customScript = CustomScript.objects.all()
    chatButton = ChatButton.objects.all().last()

    context = {
        'ContatInformation' : contatInformationData,
        'Setting' : setting,

        'CustomCode' : customCSS,
        'CustomScript' : customScript,
        'ChatButton' : chatButton,
    }
    return render(request,'page/contact.html',context)







# Email Setting    

def send_gmail(request):
    
    if request.method=="POST":
        name = request.POST.get('name')
        message_email= request.POST.get('email') 
        subject = 'Email From Your Website'
        from_message =  request.POST.get('message')

        message ='User Name : ' + name +'\n'+ 'User Email : '+message_email +'\n'+'Message : '+from_message

        send_mail(
            subject,
            message,
            message_email,
            ['habibahasun1095@mail.com'],
            fail_silently=False
        )

        return HttpResponseRedirect('contact/')
    else:
        return HttpResponse('Invalid request')


# Blog Post
def blog (request):

    blogPostData =BlogPost.objects.all().reverse()
    
    setting = Setting.objects.all().last()
    customCSS = CustomCS.objects.all()
    customScript = CustomScript.objects.all()
    chatButton = ChatButton.objects.all().last()
    context = {
        'BlogPost' : blogPostData,
        'Setting' : setting,
        'CustomCode' : customCSS,
        'CustomScript' : customScript,
        'ChatButton' : chatButton,
    }

    return render(request,'page/blog.html',context)  


def post_details(request, slug):


    siteSettingData = SiteSetting.objects.all().last()
    socilMeadiLinksData = SocialMedia.objects.all()
    post = BlogPost.objects.get(slug=slug)
    RecentPost = BlogPost.objects.filter(post_ctegory = post.post_ctegory)[:3]

    setting = Setting.objects.all().last()
    customCSS = CustomCS.objects.all()
    customScript = CustomScript.objects.all()
    chatButton = ChatButton.objects.all().last()



    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            PostComment = form.save(commit=False)
            PostComment.post = post
            PostComment.save()

            return redirect('post_details', slug=post.slug)
    else:
        form = CommentForm()



    context = {
        'SiteSetting' : siteSettingData,
        'SocialMedia' : socilMeadiLinksData,
        'post' : post,
        'RecentPost' : RecentPost,
        'form' : form,
        'Setting' : setting,
        'CustomCode' : customCSS,
        'CustomScript' : customScript,
        'ChatButton' : chatButton,
    }
    return render(request, 'page/blog-single.html', context)
 



