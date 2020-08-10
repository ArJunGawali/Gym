from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'base.html')

def gallery(request):
	return render(request,'gallery.html')

def about(request):
	return render(request,'about-us.html')



