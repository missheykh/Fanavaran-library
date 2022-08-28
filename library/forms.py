from lib_app.models import User
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password


class RegisterForm(ModelForm):
    class Meta:
        model=User
        fields=['username','password']

    def save(self,commit=True,*args,**kwargs):# Active Users After Register and Hash They Passwords
        self.instance.is_active=True
        self.instance.is_staff=True
        self.instance.password=make_password(self.cleaned_data.get('password'))
        return super().save(commit,*args,**kwargs)
