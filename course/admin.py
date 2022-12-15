from django.contrib import admin
from course.models import User
from course.models import *
from django.contrib.auth.admin import UserAdmin 
# Register your models here.

@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets =(
        (None,{"fields":("email","first_name","last_name","username","password","is_active","is_staff"),}),
    )
    list_display = ("email",)
    ordering = ("email",)

# admin.site.register(User)
admin.site.register(Post)
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)


