from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from users.models import Profile, Missing

admin.site.register(Profile)
admin.site.register(Missing)




