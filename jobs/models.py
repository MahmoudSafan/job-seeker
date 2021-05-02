from django.db import models
from django.utils.text import slugify

# Create your models here.
jobType = (
    ("Architecture and Engineering Occupations","Architecture and Engineering Occupations"),
    ("Arts, Design, Entertainment, Sports, and Media Occupations","Arts, Design, Entertainment, Sports, and Media Occupations"),
    ("Building and Grounds Cleaning and Maintenance Occupations","Building and Grounds Cleaning and Maintenance Occupations"),
    ("Business and Financial Operations Occupations","Business and Financial Operations Occupations"),
    ("Community and Social Services Occupations","Community and Social Services Occupations"),
    ("Computer and Mathematical Occupations","Computer and Mathematical Occupations"),
    ("Construction and Extraction Occupations","Construction and Extraction Occupations"),
    ("Education, Training, and Library Occupations","Education, Training, and Library Occupations"),
    ("Farming, Fishing, and Forestry Occupations","Farming, Fishing, and Forestry Occupations"),
    ("Food Preparation and Serving Related Occupations","Food Preparation and Serving Related Occupations"),
    ("Healthcare Practitioners and Technical Occupations","Healthcare Practitioners and Technical Occupations"),
    ("Healthcare Support Occupations","Healthcare Support Occupations"),
    ("Installation, Maintenance, and Repair Occupations","Installation, Maintenance, and Repair Occupations"),
    ("Legal Occupations","Legal Occupations"),
    ("Life, Physical, and Social Science Occupations","Life, Physical, and Social Science Occupations"),
    ("Management Occupations","Management Occupations")
    )
    
time =(
    ("part-time","part-time"),
    ("full-time","full-time")
)

def image_upload(instance,fileName):        # image upload customize
    imageName, extention = fileName.split(".")
    return "jobImages/%s.%s"%(instance.id,extention)

class job(models.Model):
    id = models.AutoField(primary_key= True,serialize=True)

    title = models.CharField(max_length= 50 ,null= False)

    gender = models.CharField(max_length=50, null = False)

    job_type = models.CharField(max_length = 200,choices=jobType,default="Other")

    description = models.TextField(max_length= 500, null = False)

    location = models.CharField(max_length= 70, null = False)

    vacancy = models.CharField(max_length = 200,choices=time,null=False)

    salary = models.FloatField(default=0.0, null = False)

    experiance = models.CharField(max_length = 50, null = False)

    publishedAt = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(blank= True, null= True)

    image = models.ImageField(upload_to =image_upload)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args,**kwargs)

'''

class Apply(models.Model):
    name = models.CharField(max_length=50, blanck = True, null = True)
    email = models.CharField(max_length=50, blanck = True, null = True)
    website = models.URLField( max_length=200)
    cvs = models.FileField(upload_to="cvs/")
    description = models.TextField(max_length=500, null= True)
    '''