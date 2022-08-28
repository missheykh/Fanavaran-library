from dataclasses import field
from .models import User,Book
from django import forms



class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)
    

class SearchForm(forms.Form):
    book=forms.CharField(max_length=200,required=False)
    author=forms.CharField(max_length=200,required=False)
    cat=forms.CharField(max_length=200,required=False)

   



    
