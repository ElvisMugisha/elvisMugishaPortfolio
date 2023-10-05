from django.contrib import admin
from .models import *

# Register your models here.
class AboutInfoInline(admin.TabularInline):
    model = AboutInfo
    extra = 1

class AboutSocialMediaInline(admin.TabularInline):
    model = AboutSocialMedia
    extra = 1

class AboutSkillsInline(admin.TabularInline):
    model = AboutSkills
    extra = 1

class AboutEducationInline(admin.TabularInline):
    model = AboutEducation
    extra = 1

class AboutInterestInline(admin.TabularInline):
    model = AboutInterest
    extra = 1

class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'profile', 'phone_number'
    )
    inlines = [
        AboutInfoInline, AboutSocialMediaInline, AboutSkillsInline,
        AboutEducationInline, AboutInterestInline,
    ]

class ExperienceInfoInline(admin.TabularInline):
    model = ExperienceInfo
    extra = 1

class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'company', 'location', 'role', 'start_date', 'end_date'
    )
    inlines = [ ExperienceInfoInline ]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

class FrontEndInline(admin.TabularInline):
    model = FrontEnd
    extra = 1

class BackEndInline(admin.TabularInline):
    model = BackEnd
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('project_name',)}
    list_display = (
        'project_name', 'category', 'kind', 'start_date', 'end_date'
    )
    list_filter = ('category',)
    inlines = [
        FrontEndInline, BackEndInline
    ]

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service_name', 'created_at', 'updated_at'
    )

admin.site.register(About, AboutAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
