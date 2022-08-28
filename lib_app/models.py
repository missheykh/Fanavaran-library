from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Author(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self,*args,**kwargs):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self,*args,**kwargs):
        return self.name


class Book(models.Model):
 title=models.CharField(max_length=200)
 author=models.ManyToManyField(Author,through='Publication',related_name='auth_book')
 cat=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='cat_book')
 slug_title=models.SlugField(blank=True,allow_unicode=True)

 def save(self, *args,**kwargs) -> None:
    if not self.slug_title:
        self.slug_title=slugify(self.title,allow_unicode=True)
    super().save(*args,**kwargs)

 def __str__(self,*args,**kwargs):
        return self.title


class Publication(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='book_pub')
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='auth_pub')
    pub_name=models.CharField(max_length=200)
    pub_date=models.IntegerField()
    img=models.ImageField(upload_to='book_img/',null=True,blank=True)
    user=models.ManyToManyField(User,through='Loan',related_name='user_pub')

    class Meta:
        ordering=['pub_date']

    def __str__(self,*args,**kwargs):
        return f"{self.book}:{self.pub_name}"


class Loan(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='user_loan')
    book=models.ForeignKey(Publication,on_delete=models.DO_NOTHING,related_name='book_loan')
    loan_date=models.DateField()
    return_date=models.DateField()
    desc=models.TextField(null=True,blank=True)

    def __str__(self,*args,**kwargs):
        return f"{self.user}:{self.book}"

