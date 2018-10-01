from django  import forms
from.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = [
		"title",
		"image",
		"content",
		

		]

class Login_form(forms.Form):
	First_name=forms.CharField(max_length=30,required=False)
	Last_name= forms.CharField(max_length=20)
	email_id=forms.EmailField(max_length=125)
	password=forms.CharField(widget=forms.PasswordInput)

	def Clean_First_name(self):
		First_name=self.cleaned_data['First_name']
		return First_name



	def Clean_Last_name(self):
		Last_name=self.cleaned_data['Last_name']
		return Last_name


		
	def Clean_email_id(self):
		email=self.cleaned_data['email_id']	
		return email

	
	def Clean_password(self):
		password=self.cleaned_data('password')
		return password



	def save(self,commit=True):
		user=User.objects.create_User(
			self.cleaned_data['First_name'],
			self.cleaned_data['Last_name'],
			self.cleaned_data['email_id'],
			self.cleaned_data['password'],

			)
		return user







#class Person(for
		