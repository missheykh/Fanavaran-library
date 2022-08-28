from django.shortcuts import render
from .forms import RegisterForm
from lib_app.models import User


def register(request):
    context={}
    if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                _username=form.cleaned_data.get('username','')
                if User.objects.filter(username=_username).exists():
                    return render(request,'index.html',{"msg":"username already exist"})
                else:
                    form.save()
                    
                    return render(request,'index.html',{"form":form,"msg":"user created sucessfully Now you should login"})
            else:
                return render(request,'index.html',{"form":form,"msg":form.errors})
    else:
        form=RegisterForm()
        context['form']=form
        return render(request,'index.html',context)
    