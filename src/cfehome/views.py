from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request):
    queryset = PageVisit.objects.filter(path=request.path)
    PageVisit.objects.create(path=request.path)
    return render(request,'index.html',context={'queryset':queryset})