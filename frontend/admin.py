from django.contrib import admin


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

#Email Setting
from .models import EmailSetting

# BlogPost
from .models import BlogPost
from .models import Comment
from .models import BlogCategory

# Custom Code
from .models import CustomCS
from .models import CustomScript

# setting
from .models import Setting

# Social media Chat Button
from .models import ChatButton  






# Register your models here.



class siteSettingAdmin(admin.ModelAdmin):
    
    list_filter = ['owner_name']
    list_per_page = 2
    search_fields = ['owner_name','owner_Profession']

    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        return obj.logo_preview

    logo_preview.short_description = 'Thumbnail Preview'
    logo_preview.allow_tags = True
    list_display = ['owner_name','owner_Profession','logo']

admin.site.register(SiteSetting,siteSettingAdmin)

class activePages(admin.ModelAdmin):
    list_display = ['about_page','resume_page','portfolio_page','blog_page','contact_page'] 
admin.site.register(ActivePage,activePages)


class socialMedia(admin.ModelAdmin):
    list_display = ['platform_name','link']
    list_filter = ['platform_name']
    list_per_page = 10
    search_fields = ['platform_name']
admin.site.register(SocialMedia,socialMedia)

# About Page
class UserProfile(admin.ModelAdmin):
    list_display = ['profile_image','about_content']
    list_filter = ['about_content']
    list_per_page = 2
admin.site.register(AboutMe,UserProfile)


class service(admin.ModelAdmin):
    list_display = ['service_name','icon']
    list_filter = ['service_name']
    list_per_page = 10
    search_fields = ['service_name']
admin.site.register(Service,service)


class workProcces(admin.ModelAdmin):
    list_display = ['procces_name','icon']
    list_filter = ['procces_name']
    list_per_page = 10
    search_fields = ['procces_name']
admin.site.register(WorkProcces,workProcces)


class workWith(admin.ModelAdmin):
    list_display = ['clients_name','logo']
    list_filter = ['clients_name']
    list_per_page = 10
    search_fields = ['clients_name']
admin.site.register(WorkWith,workWith)

class achivement(admin.ModelAdmin):
    list_display = ['detials','icon']
    list_filter = ['detials']
    list_per_page = 10
admin.site.register(Achivement,achivement)

# Resume Page
class workHistory(admin.ModelAdmin):
    list_display = ['designation','company_name','starting','ending']
    list_filter = ['designation','company_name']
    list_per_page = 10
    search_fields = ['designation','company_name']
admin.site.register(WorkHistory,workHistory)

class education(admin.ModelAdmin):
    list_display = ['subject','institute_name','starting','ending']
    list_filter = ['subject','institute_name']
    list_per_page = 10
    search_fields = ['subject','institute_name']
admin.site.register(Education,education)


class skill(admin.ModelAdmin):
    list_display = ['platform_name','skill_percentage']
    list_filter = ['platform_name']
    list_per_page = 10
    search_fields = ['platform_name']
admin.site.register(Skill,skill)


class testimonial(admin.ModelAdmin):
    list_display = ['clients_name','clients_designation','clients_image','company_name']
    list_filter = ['clients_name','clients_designation','company_name']
    list_per_page = 10
    search_fields = ['clients_name','clients_designation','company_name']
admin.site.register(Testimonial,testimonial)

class curriculumVitae(admin.ModelAdmin):
    list_display = ['publish_date','cv']
    list_filter = ['publish_date']
    list_per_page = 3
    search_fields = ['publish_date']
admin.site.register(CurriculumVitae,curriculumVitae)


# Portfolio Page
class portfolioMenu(admin.ModelAdmin):
    list_display = ['name','category_class']
    list_filter = ['name','category_class']
    list_per_page = 10
    search_fields = ['name','menu_class']
admin.site.register(PortfolioCategory,portfolioMenu)


class portfolioItem(admin.ModelAdmin):
    list_display = ['project_name','category_class','image']
    list_filter = ['project_name','category_class']
    list_per_page = 10
    search_fields = ['project_name','category_class']
admin.site.register(PortfolioItem,portfolioItem)



#Contact Page
class contatInformation(admin.ModelAdmin):
    list_display = ['details','icon']
    list_per_page = 10
admin.site.register(ContatInformation,contatInformation)


#Email Setting
class emailSetting(admin.ModelAdmin):
    list_display = ['email_host','email_port','user_email']
    list_filter = ['email_host','email_port','user_email']
    list_per_page = 5
    search_fields = ['email_host','email_port','user_email']
admin.site.register(EmailSetting,emailSetting)


# BlogPost

class blogCategory(admin.ModelAdmin):
    list_display = ['post_category_name','publish_date']
    list_filter = ['post_category_name','publish_date']
    list_per_page = 10
    search_fields = ['post_category_name','publish_date']
admin.site.register(BlogCategory,blogCategory)

class blogPost(admin.ModelAdmin):
    list_display = ['title','author','post_ctegory','post_date']
    list_filter = ['title','author','post_ctegory']
    list_per_page = 10
    search_fields = ['title','author','post_ctegory']
admin.site.register(BlogPost,blogPost)

class comment(admin.ModelAdmin):
    list_display = ['name','body','replay','date_added']
    list_filter = ['name','date_added']
    list_per_page = 30
    list_editable = ('replay',)
    search_fields = ['name','date_added']
admin.site.register(Comment,comment)

# Custom Code
class customCode(admin.ModelAdmin):
    list_display = ['code','active','publish_date']
    list_filter = ['active','publish_date']
    list_per_page = 10
    list_editable = ('active',)
    search_fields = ['code','publish_date']
admin.site.register(CustomCS,customCode)

class customScript(admin.ModelAdmin):
    list_display = ['code','active','publish_date']
    list_filter = ['active','publish_date']
    list_per_page = 10
    list_editable = ('active',)
    search_fields = ['code','publish_date']
admin.site.register(CustomScript,customScript)

# Social media Chat Button 
class chatButton(admin.ModelAdmin):
    list_display = ['name','publish_date']
    list_filter = ['name','publish_date']
    list_per_page = 3
    search_fields = ['name','publish_date']
admin.site.register(ChatButton,chatButton)


# setting
class setting(admin.ModelAdmin):
    list_display = ['author','Website_title','copyright','keywords']
    list_filter = ['author','Website_title']
    list_per_page = 5
    search_fields = ['author','Website_title']
admin.site.register(Setting,setting)

# admin header and title modification
admin.site.site_header = "Admin DashBoard"
admin.site.site_title = "Website"
admin.site.index_title = ''# admin header and title modification




