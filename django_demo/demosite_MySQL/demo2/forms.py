from django import forms
from .models import Location

class CreateForm(forms.Form):
    id_location = forms.IntegerField(
        label='ID',
        widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'integer'}), 
    )
    country = forms.CharField()
    city = forms.CharField()

    def clean_country(self, *args, **kwargs): #覆寫, 名稱須用clean_
        country = self.cleaned_data.get('country') #取得表單所填寫的資料
        if country=='中國台灣': #驗證
            raise forms.ValidationError('不得使用中國台灣')
        return country

class CreateModelForm(forms.ModelForm):
    class Meta:
        model = Location
        #fields = ['id_location','country']
        fields = '__all__'
        #exclude = ['city'] #排除
        labels = {
            'id_location': 'ID',
        }
        widgets = {
            'id_location': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'integer'}),
        }        

    def clean_country(self, *args, **kwargs): #覆寫, 名稱須用clean_
        country = self.cleaned_data.get('country') #取得表單所填寫的資料
        if country=='中國台灣': #驗證
            raise forms.ValidationError('不得使用中國台灣')
        return country


class LoginForm(forms.Form):
    username = forms.CharField(
        label = "", # hidden label
        widget = forms.TextInput(attrs={'placeholder': 'Username'}) # set 
    )
    password = forms.CharField(
        label = "",
        widget = forms.PasswordInput(attrs={"placeholder": "Password"})
    )


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm): #繼承
    username = forms.CharField(
        label='帳號',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )
    email = forms.EmailField(
        label='電子郵件',
        widget=forms.EmailInput(attrs={'class': 'form-control mb-2'})
    )
    password1 = forms.CharField(
        label='密碼',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-2'})
    )
    password2 = forms.CharField(
        label='密碼確認',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-2'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        cleaned_data = super().clean() #繼承
        email = cleaned_data.get('email')
        if User.objects.filter(email=email): #驗證
            raise forms.ValidationError('email exist.')
        return email

from django.contrib.auth.forms import PasswordResetForm
class NewPasswordResetForm(PasswordResetForm): #繼承
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class":"form-control form-control-lg mb-3",
            "placeholder": "Username",})
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "class":"form-control form-control-lg mb-3",
            "placeholder": "Email",})
    )

    def clean_username(self): #覆寫 -> field.errors
        cleaned_data = super().clean() #繼承
        username = cleaned_data.get('username')
        users = User.objects.filter(username=username)
        if not users: #驗證
            raise forms.ValidationError('帳號不存在')
        return username

    def clean_email(self): #覆寫 -> field.errors
        cleaned_data = super().clean() #繼承
        email = cleaned_data.get('email')        
        mails = User.objects.filter(email=email)
        if not mails: #驗證
            raise forms.ValidationError('信箱不存在')
        return email

    def clean(self): #覆寫 -> non_field_errors
        cleaned_data = super().clean() #繼承
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        u = User.objects.filter(username=username,email=email)        
        if not u: #驗證
            raise forms.ValidationError('帳號與信箱不符合')
        return cleaned_data