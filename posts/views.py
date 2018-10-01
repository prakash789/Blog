from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from.forms import PostForm
from.models import Post
from django.contrib.auth import authenticate, login
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from.forms import Login_form
import logging
from django.forms import ValidationError
from django.contrib.auth.models import User

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

#def post_home(request):
	#	return HttpResponse("<h1>Hello</h1>")
def register(request):
	if request.method =='POST':
		f=Login_form(request.POST)
		if f.is_valid():
			userObj = f.cleaned_data
			First_name=userObj['First_name']
			Last_name=userObj['Last_name']
			email_id=userObj['email_id']
			password=userObj['password']
			username=First_name + Last_name
			

			if not(User.objects.filter(first_name=First_name).exists()or User.objects.filter(last_name=Last_name).exists()or User.objects.filter(email=email_id).exists()):
				User.objects.create_user(username =username,first_name=First_name,last_name=Last_name,email=email_id,password=password)
				user = authenticate(username = username, password = password)
			
				login(request,user)
				return HttpResponseRedirect('/')
	   	else:
	    	 raise f.ValidationError('Looks like a username with that email or password already exists')
	else:
		f=Login_form()		
	return render(request,"register.html",{'f':f})



def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	print form

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"successful created")

	else:
		messages.error(request,"not succesful created")
	#if request.method =="POST":
		#print "title is " + request.POST.get("title")
	
	context ={
		"form":form,
	}
	return render (request,"post_form.html",context)

def post_details(request,id):
	instance=get_object_or_404(Post,id=id)
	context ={
	"abc":instance.title,
	"ab":instance,

	}
	return render (request,"post_detail.html",context)



def post_list(request):
	queryset_list=Post.objects.all()
	paginator = Paginator(queryset_list, 25)
	 # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset= paginator.page("page")
   	except PageNotAnInteger:
 		queryset=paginator.page(1)
  	except EmptyPage:
  		queryset=paginator.page(paginator.num_pages)
		#print queryset
	context ={
		"title":"list",
		"object_list":queryset

	}
	return render (request,"post_list.html",context)
	#return HttpResponse("<h1>list</h1>")

def post_update(request,id):
	instance=get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	print request.FILES
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()

	context ={
	"title":instance.title,
	"intance":instance,
	"form":form,

	}
	return render(request,"post_form.html",context)
	

def post_delete(request,id=None):

	instance=get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"successful deleted")
	return redirect("posts:list")


def test_cookie(request):
	
	if not request.COOKIES.get('color'):
		response=HttpResponse("Cookie Set")
		response.set_cookie('color','blue')
		return response
	else:
		return HttpResponse("your favorite color is {0}".format(request.COOKIES['color']))

def track_user(request):
	response=render(request,"track_user.html")
	if not request.COOKIES.get('visits'):
		response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
		#response=HttpResponse("this is your first visit i trace your visit in my site for thnks to visit my site")

	else:
		visits= int(request.COOKIES.get('visits'))+1
		response=render(request,"track_user.html")
	return response
# Create your views here.
