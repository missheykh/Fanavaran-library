from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import LoginForm,SearchForm
from .models import Book,Publication
from django.contrib.auth import login as _login, authenticate,logout as _logout


def login(request):# Login Registered Users Or Get Errors For Unregistered Users
    error=''
    if request.method=='GET':
        form=LoginForm()
        return render(request,'lib_app/login.html',{'form':form})
    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            _username=form.cleaned_data.get('username','')
            _password=form.cleaned_data.get('password','')
            user=authenticate(request,username=_username,password=_password)
            if user:
                _login(request,user)
                return redirect('lib_app:booklist')
            else:
                error='Please Enter Username and Passwork Correctly Or Register First'
                return render(request,'lib_app/login.html',{'form':form,'error':error})
        else:
            error=form.errors
            return render(request,'lib_app/login.html',{'form':form,'error':error})
                

class BookList(ListView):# List All Books With Some Attributes
    model=Publication
    template_name='lib_app/booklist.html'
    context_object_name='books'
    paginate_by=12
    
        
def logout(request):# Logout The Loggedin User
    form = LoginForm()
    context={"form":form,"msg":"you loged out"}
    _logout(request)
    return render(request,'lib_app/login.html',context)


def find(request,**kwargs):# Doing Filter By input Arguments Like Book title, Book Author Or Book Category
    _book=kwargs.get('book','')
    _author=kwargs.get('author','')
    _cat=kwargs.get('cat','')
    books=''
    error=''
    msg='please fill just  one filed'
    if not _book and not  _author and not  _cat: # If All 3 Fields Will Be Empty
        error=msg
    elif _book:
        if _author or _cat: # For Suring Just book Field IS Filled
            error=msg
        else:
            books=Publication.objects.filter(book__title__icontains=_book)
    elif _author:
        if _book or _cat:# For Suring Just author Field IS Filled
            error=msg
        else:
            books=Publication.objects.filter(author__name__icontains=_author)
    elif _cat:
        if _book or _author:# For Suring Just category Field IS Filled
            error=msg
        else:
            books=Book.objects.filter(cat__name__icontains=_cat)
    return {'books':books,'error':error}
       

def search(request):# Create Search Form and render the search.html and Using The find function
    if request.method=='GET':
        searchform=SearchForm()
        return render(request,'lib_app/search.html',{'searchform':searchform})
    else:
        searchform=SearchForm(request.POST)
        if searchform.is_valid():
            error=''
            books=''
            print(searchform.cleaned_data)
            _book=searchform.cleaned_data.get('book','')
            _author=searchform.cleaned_data.get('author','')
            _cat=searchform.cleaned_data.get('cat','')
            find_output=find(request,book=_book,author=_author,cat=_cat)
            books=find_output.get('books')
            error=find_output.get('error')
            print(f"boooooooooooks:{books}")
            return render(request,'lib_app/search.html',{'searchform':searchform,'books':books,'error':error})
        else:
            error=searchform.errors
            return render(request,'lib_app/search.html',{'searchform':searchform,'error':error})



