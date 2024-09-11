from django.contrib import admin
from .models import Post
from .models import Category
from .models import Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["first_name","last_name","username", "email","password","image","dob","gender","mobile"]

admin.site.register(User, CustomUserAdmin)