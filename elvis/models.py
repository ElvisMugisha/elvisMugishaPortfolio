from django.db import models

# Create your models here.

class About(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    profile = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    profile_pic = models.ImageField(upload_to='images/about')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return f"self.first_name + self.last_name"

class AboutInfo(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, blank=True, null=True, default=None)
    description = models.TextField()

    class Meta:
        verbose_name = "About Me Info"
        verbose_name_plural = "About Me Infos"

class AboutSocialMedia(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE ,blank=True,null=True )
    github = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"

class AboutSkills(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, blank=True, null=True, default=None)
    skill = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class AboutEducation(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, blank=True, null=True, default=None)
    title = models.CharField(max_length=200, blank=True, null=True)
    option = models.CharField(max_length=200, blank=True, null=True)
    where = models.CharField(max_length=200, blank=True, null=True)
    when = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

class AboutInterest(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, blank=True, null=True, default=None)
    interest = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Interest"
        verbose_name_plural = "Interests"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Experience"
        verbose_name_plural = "Experiences"

class ExperienceInfo(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, blank=True, null=True, default=None)
    description = models.TextField()

    class Meta:
        verbose_name="Description"
        verbose_name_plural = "Descriptions"

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    kind = models.CharField(max_length=200, default="")
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    live = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/projects')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.project_name

class FrontEnd(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name ="Front End"
        verbose_name_plural = "Front End"

class BackEnd(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE ,blank=True,null= True,default= None )
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Back End"
        verbose_name_plural = "Back End"

class Service(models.Model):
    service_name  = models.CharField ( max_length=150 )
    icon = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.service_name
