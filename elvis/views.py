from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # About related
    about_me = About.objects.all()
    infos = AboutInfo.objects.all()
    social_medias = AboutSocialMedia.objects.all()
    skills = AboutSkills.objects.all()
    educations = AboutEducation.objects.all().order_by('-id')
    interests = AboutInterest.objects.all()

    # Experience related
    experiences = Experience.objects.all().order_by('-id')
    expe_infos = ExperienceInfo.objects.all()

    # Category related
    categories = Category.objects.all()

    # Project related
    projects = Project.objects.all().order_by('-id')
    fronts = FrontEnd.objects.all()
    backs = BackEnd.objects.all()

    # Service related
    services = Service.objects.all()

    context = {
        'about_me': about_me, 'infos': infos, 'social_medias': social_medias,
        'skills': skills, 'educations': educations, 'interests': interests,
        'experiences': experiences, 'expe_infos': expe_infos, 'categories': categories,
        'projects': projects, 'fronts': fronts, 'backs': backs,
        'services': services,
    }

    template_name = 'elvis/index.html'
    return render(request, template_name, context)
