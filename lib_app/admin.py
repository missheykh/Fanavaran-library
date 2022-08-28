from atexit import register
from django.contrib import admin
from .models import User,Publication,Book,Author,Loan,Category
from django.contrib.auth import get_user_model

# Register your models here.

admin.site.register(get_user_model())
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(Loan)
admin.site.register(Category)
