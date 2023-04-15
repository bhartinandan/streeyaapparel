from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

#####################################
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(max_length=63,widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    
class AddressForm(forms.Form):
	name = forms.CharField(max_length=100,
			widget=forms.TextInput(attrs={'placeholder': 'Name'}),
			error_messages={"required": "Please enter your name"})
	mobile_number = forms.CharField(max_length=10,
				 min_length=10,
				 widget=forms.NumberInput(attrs={'placeholder': 'Mobile Number'}),
			error_messages={"required": "Please enter your mobile Number"})
	alternate_mobile_number = forms.CharField(max_length=10,
				 min_length=10,
				 widget=forms.NumberInput(attrs={'placeholder': 'Alternate mobile Number'}),
			error_messages={"required": "Please enter your mobile Number"})
	pin_code = forms.CharField(max_length=6,
				 min_length=6,
				 widget=forms.NumberInput(attrs={'placeholder': 'Zip/Pin code'}),
			error_messages={"required": "Please enter your Zip/Pin code"})
	hno = forms.CharField(max_length=200,
				widget=forms.TextInput(attrs={'placeholder': 'house number'}))
	city = forms.CharField(max_length=50,
				widget=forms.TextInput(attrs={'placeholder': 'city'}))
	state = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={'placeholder': 'state'}))
	country = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={'placeholder': 'country'}))
	area = forms.CharField(max_length=300,
				widget=forms.TextInput(attrs={'placeholder': 'address'}))

	
	

