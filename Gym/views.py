from django.shortcuts import render
from .forms import imgform
from django.shortcuts import redirect
from .models import img
from django.core.files.storage import FileSystemStorage
from .settings import MEDIA_URL

# Create your views here.

URL = 'http://127.0.0.1:8000/'

def index(request):
	return render(request,'base.html')

def gallery(request):
	if request.method =="GET":
		form = imgform()
		images = img.objects.all()
		return render(request,'gallery.html',{'form': form , 'images': images ,'URL':URL , 'MEDIA_URL' : MEDIA_URL})
	elif request.method=="POST":

		form = imgform(request.POST,request.FILES)
		scode=request.POST.get('title')
		images = img.objects.all()
		# myfile = request.FILES['img']
		if scode=='G08H10C00':

			fs=FileSystemStorage()

			if form.is_valid():
				form.save()
				# imgv=img(request.GET,request.FILES)
				# imgv.save()
			return redirect('gallery')
		else:
			msg = 'Wrong Security Code.'
			return render(request,'gallery.html',{'msg':msg,'images':images , 'form': form })

def deleteImg(request):
	form = imgform(request.POST,request.FILES)
	images = img.objects.all()
	if request.method=="POST":
		
		if request.POST.get('sc') == 'G08H10C00':
			idk=request.GET.get('idk')
			img.objects.filter(id=idk).delete()
			return redirect('gallery')
		else:
			msg = 'Wrong Security Code.'
			return render(request,'gallery.html',{'msg':msg,'images':images , 'form': form })
	else:
		return render(request,'gallery.html',{'images':images , 'form': form })



def about(request):
	return render(request,'about-us.html')

def sample(request):
	if request.method =="GET":
		form = imgform()
		images = img.object.all()
		
		return render(request,'sample.html',{'form': form ,'images': images})
	else:

		form = imgform(request.POST,request.FILES)
		# myfile = request.FILES['img']
		fs=FileSystemStorage()

		if form.is_valid():
			form.save()
			# imgv=img(request.GET,request.FILES)
			# imgv.save()
		return redirect('gallery')



