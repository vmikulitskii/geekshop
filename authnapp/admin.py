from django.contrib import admin
from .models import ShopUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class ShopUserAdmin(UserAdmin):
    pass


admin.site.register(ShopUser, ShopUserAdmin)