
from django.contrib import admin
from django.urls import path
from .views import login,BookList,logout,search

app_name='lib_app'

urlpatterns = [
    path('login/',login,name='login'),
    path('booklist/',BookList.as_view(),name='booklist'),
    path('logout',logout,name='logout'),
    path('search/',search,name='search')
]
