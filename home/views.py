from django.shortcuts import render
from django.http import HttpResponse
from create_post.models import Contactdetails,Whatwedo,Addimage
# Create your views here.

class basic_details:
    contact=Contactdetails.objects.get(id=1)
    trustMail=contact.trustMail
    trustAddress=contact.trustAddress
    trustOrg=contact.trustOrg
    trustPhonenumber=contact.trustPhonenumber
    trustFrontimage=contact.trustFrontimage

def index(request):
    b=basic_details()
    selection=Whatwedo.objects.all()
    data={
        "trustMail":b.trustMail,
        "trustAddress":b.trustAddress,
        "trustOrg":b.trustOrg,
        "trustPhonenumber":b.trustPhonenumber,
        "trustFrontimage":b.trustFrontimage,
        "selection":selection,
    }
    return render(request,"index/index.html",data)

def detailswhatwedo(request):
    b=basic_details()
    search=request.GET.get('search')
    s=request.GET.get('s')
    selection=Whatwedo.objects.all().exclude(pk=s)
    value=Whatwedo.objects.get(pk=s)
    images=Addimage.objects.filter(projectid=s)
    data={
        "trustMail":b.trustMail,
        "trustAddress":b.trustAddress,
        "trustOrg":b.trustOrg,
        "trustPhonenumber":b.trustPhonenumber,
        "trustFrontimage":b.trustFrontimage,
        "selection":selection,
        "heading":value.name,
        "content":value.content,
        "frontimage":value.image,
        "images":images,
    }
    return render(request,"index/detailswhatwedo.html",data)

def sample2(request):
    search=request.GET.get('search')
    s=request.GET.get('s')
    
    return HttpResponse(search+""+str(s))


def error_404_view(request, exception):
    return render(request,'404.html')
    

def error_500_view(request, exception):
    return render(request,'500.html')