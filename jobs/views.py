from django.shortcuts import render
from django.core.paginator import Paginator

from .models import job
# Create your views here.

def jobs(request):
    jobs = job.objects.all()

    paginator = Paginator(jobs, 2) # Show 1 contact per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj}

    return render(request,'joblist.html',context)

def job_details(request,slug):
    job_detail = job.objects.get(slug = slug)
    context = {"job" : job_detail}
    return render(request,'job_detail.html',context)