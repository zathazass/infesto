from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.models import User
from . models import Profile

class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="",widget=forms.PasswordInput)
    username.widget.attrs.update({'class':'form-control','placeholder':'User Name'})
    password.widget.attrs.update({'class':'form-control','placeholder':'Password'})
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username,password=password)

        if not user:
            raise forms.ValidationError('username or Password is invalid')

        return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="")
    email = forms.EmailField(label='')
    password = forms.CharField(widget=forms.PasswordInput,label="")
    confirm_password = forms.CharField(widget=forms.PasswordInput,label="")

    username.widget.attrs.update({'class':'form-control','placeholder':'User Name'})
    email.widget.attrs.update({'class':'form-control','placeholder':'User Email'})
    password.widget.attrs.update({'class':'form-control','placeholder':'Password'})
    confirm_password.widget.attrs.update({'class':'form-control','placeholder':'Confirm Password'})

    class Meta:
        model = User
        fields = [

            'username',
            'email',
            'password',
            'confirm_password',
        ]
    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        email_already = User.objects.filter(email=email)
        if email_already.exists():
            raise forms.ValidationError('Email already exists')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password didn't match")
        else:
            return super(UserRegisterForm,self).clean(*args,**kwargs)

class ProfileForm(forms.ModelForm):
    team_name = forms.CharField(label='')
    student_name = forms.CharField(label='')
    member_name = forms.CharField(label='')
    member_name2 = forms.CharField(label='')
    college = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label='')
    phone = forms.CharField(label='')
    team_name.widget.attrs.update({'class':'form-control','placeholder':'Team Name'})
    member_name.widget.attrs.update({'class':'form-control','placeholder':'Member Name 1'})
    member_name2.widget.attrs.update({'class':'form-control','placeholder':'Member Name 2'})
    student_name.widget.attrs.update({'class':'form-control','placeholder':'Your Name'})
    college.widget.attrs.update({'class':'form-control','placeholder':'college Name'})
    phone.widget.attrs.update({'class':'form-control','placeholder':' Your Mobile No'})
    class Meta:
        model = Profile
        fields = [
            'team_name',
            'student_name',
            'member_name',
            'member_name2',
            'college',
            'phone',

        ]
class UserForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            #'email',
            #'first_name',
            #'last_name',
        ]
