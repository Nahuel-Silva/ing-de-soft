from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

class UserRegisterForm(UserCreationForm):
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['name', 'lastname', 'username', 'email']
        help_texts = { k:"" for k in fields }

class PostForm(forms.ModelForm):
    title = forms.CharField()
    imagen_album = forms.ImageField()

    class Meta:
        model = Post
        fields = ['title', 'imagen_album']