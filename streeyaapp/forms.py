from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from streeyaapp.models import *


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
	
class SignupuserForm(forms.Form):
    username = forms.CharField(max_length=63,
                               widget=forms.TextInput(attrs={'placeholder': 'Email id/Mobile number'})
                                             )

class UserotpForm(forms.Form):
    otp = forms.CharField(max_length=6,
				 min_length=6,
				 widget=forms.NumberInput(attrs={'placeholder': 'otp'}),
			error_messages={"required": "Please enter your otp"})
	
class PasswordForm(forms.Form):
    password = forms.CharField(max_length=63,widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    

########################################################
########################## ADMIN #######################
########################################################

class MobViewBannerForm(forms.Form):
      img = forms.ImageField()
      
class MultipleImageField(forms.FileField):
    def to_python(self, data):
        if not data:
            return []
        elif isinstance(data, list):
            return [super().to_python(item) for item in data]
        else:
            return [super().to_python(data)]
        
class AddDataForm(forms.Form):
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all(),
                                          widget=forms.Select(attrs={'class':'form-select form-select-sm mb-3','aria-label':'.form-select-sm example'}))
    type = forms.ModelChoiceField(queryset=Type.objects.all(),
                                          widget=forms.Select(attrs={'class':'form-select form-select-sm mb-3','aria-label':'.form-select-sm example'}))
    product_id = forms.ModelChoiceField(queryset=ProductId.objects.all(),
                                          widget=forms.Select(attrs={'class':'form-select form-select-sm mb-3','aria-label':'.form-select-sm example'}))
    name = forms.CharField(max_length=150,
                           widget=forms.TextInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Name'}))
    original_price = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Original Price'}))
    offer_price = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Offer Price'}))
    description = forms.CharField(max_length=500,
				widget=forms.Textarea(attrs={'class':'form-control form-control-sm','aria-label':'With textarea'}))
    sticker_value = forms.CharField(max_length=6,
				 widget=forms.TextInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example'}))
    xs_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of XS Items'}))
    s_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of S Items'}))
    m_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of M Items'}))
    l_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of L Items'}))
    xl_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of XL Items'}))
    two_xl_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of 2XL Items'}))
    three_xl_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of 3XL Items'}))
    four_xl_count = forms.CharField(max_length=10,
				 widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','aria-label':'.form-control-sm example','placeholder': 'Number of 4XL Items'}))
    images = MultipleImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control form-control-sm bg-dark','aria-label':'.form-control-sm example','multiple': True}))
    available = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))