from django.shortcuts import render,HttpResponse
from create_post.models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.
def login(request):
    return render(request,'Admin/adminLogin.html')


def signup(request):
    return render(request,'Admin/signup.html')

    
def trust_admin_login(request):
    if request.method =="POST":
        email=request.POST.get('adminGmail')
        password=request.POST.get('adminPassword')
        print(email,password)
        if email=="1@gmail.com" and password =='hello':
            data={
                "email":email,
                "password":password
            }
            return render(request,"admin_html/addimage.html",data)
        else:
            return render(request,"Admin/adminLogin.html",{"msg":"Incorrect Details"})

    else:            
        return render(request,"Admin/adminLogin.html",{"msg":"Please check serverside"})


def addimage(request):
    selection=Whatwedo.objects.all()
    return render(request,'admin_html/addimage.html',{"selection":selection})

def addwhatwedo(request):
    return render(request,'admin_html/addwhatwedo.html')

def headingcontentimage(request):
    selection=Whatwedo.objects.all()
    return render(request,'admin_html/headingcontentimage.html',{"selection":selection})

def managephotos(request):
    images=Addimage.objects.all()
    return render(request,'admin_html/managephotos.html',{"images":images})

def frontimagechange(request):
    return render(request,'admin_html/frontimagechange.html')
def contactusform(request):
    contact=Contactdetails.objects.get(pk=1)
    return render(request,'admin_html/contactusform.html',{"contact":contact})

def listofwhatwedo(request):
    selection=Whatwedo.objects.all()
    return render(request,'admin_html/listofwhatwedo.html',{"selection":selection})

def contactusform_sumbit(request):
        if request.method =="POST":
            trustMail=request.POST.get('trustMail')
            trustAddress=request.POST.get('trustAddress')
            trustOrg=request.POST.get('trustOrg')
            trustPhonenumber=request.POST.get('trustPhonenumber')
            Contactdetails.objects.filter(pk=1).update(trustMail=trustMail,trustAddress=trustAddress,trustOrg=trustOrg,trustPhonenumber=trustPhonenumber)
            return render(request,'admin_html/contactusform.html',{"msg":"Update Success fully!!"})
        else: 
            return HttpResponse("something went to Wrong")


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def frontimage_sumbit(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        Contactdetails.objects.filter(pk=1).update(trustFrontimage=uploaded_file_url)
        return render(request,'admin_html/frontimagechange.html',{"msg":"Update Success fully!!"}) 
    return HttpResponse("error")

def addwhatwedo_submit(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        p = Whatwedo(name=name)
        p.save()
        return render(request,'admin_html/addwhatwedo.html',{"msg":"Added Success fully!!"}) 
    return HttpResponse("error")
    
def headingcontentimage_submit(request):
    if request.method == 'POST' and request.FILES['myfile']:
        select=request.POST.get('select')
        content=request.POST.get('content')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        selection=Whatwedo.objects.all()
        if content=="":
            Whatwedo.objects.filter(pk=select).update(image=uploaded_file_url)
            return render(request,'admin_html/headingcontentimage.html',{"msg":"image updated Success fully!!","selection":selection}) 
        if content=="" and uploaded_file_url=="":
            return render(request,'admin_html/headingcontentimage.html',{"msg":"no change "}) 
        Whatwedo.objects.filter(pk=select).update(image=uploaded_file_url,content=content)
        return render(request,'admin_html/headingcontentimage.html',{"msg":"Updated Success fully!!","selection":selection})  
    return HttpResponse("error")


def listdelete(request):
    if request.method == 'GET':
        project=request.GET.get('s')
        if Whatwedo.objects.filter(pk=project).delete():
            selection=Whatwedo.objects.all()
            return render(request,'admin_html/listofwhatwedo.html',{"msg":"Deleted Success fully!!","selection":selection})  
        return HttpResponse("error")
    return HttpResponse("error")

def imagedelete(request):
    if request.method == 'GET':
        project=request.GET.get('s')
        if Addimage.objects.filter(pk=project).delete():
            images=Addimage.objects.all()
            return render(request,'admin_html/managephotos.html',{"msg":"Deleted Success fully!!","images":images})  
        return HttpResponse("error")
    return HttpResponse("error")

def sample(request):
    if request.method == 'POST' and request.FILES['myfile']:
        select=request.POST.get('select')
        date=request.POST.get('date')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        selection=Whatwedo.objects.all()
        p=Addimage(projectid=select,image=uploaded_file_url,date=date)
        p.save()
        return render(request,'admin_html/addimage.html',{"msg":"Updated Success fully!!","selection":selection})  
    return HttpResponse("error")
    
