from __future__ import unicode_literals


from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

from django.contrib.auth.models import User


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=66)
    email = models.EmailField(_('email address'), unique=True )
    first_name = models.CharField(_('first_name'), max_length=30)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True) 
    last_name=models.CharField(_('last_name'),max_length=15)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password","first_name","last_name","is_active","is_staff","username"]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs) 

User = get_user_model()

# class Customer(models.Model):
#      user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
#      name = models.CharField(max_length=15,null=True)
#      email=models.CharField(max_length=100,null=True)
    
#      def __str__(self):
#         return self.name

class Post(models.Model):
    title = models.CharField(max_length=15,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title +'|'+ str(self.author)


#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
#     data_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False,null=True,blank=True)
#     transaction = models.CharField(max_length=200,null=True)

#     def __str__(self):
#         return str(self.id)


# class OrderItem(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
#     order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
#     quantity = models.IntegerField(default=0,null=True,blank=True)
#     data_joined = models.DateTimeField(auto_now_add=True)


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
#     order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
#     address = models.CharField(max_length=200,null=True)
#     city = models.CharField(max_length=100,null=True)
#     state = models.CharField(max_length=200,null=True)
#     zipcode = models.CharField(max_length=11,null=True)
#     data_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address


