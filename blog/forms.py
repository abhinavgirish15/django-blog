from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Post
from .models import User
from .models import Category
from .models import Tag
from django_ckeditor_5.widgets import CKEditor5Widget
# from .models import Comment
from .models import Comment
from .models import Reply


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags', 'thumbnail', 'main_image')
        widgets = {
              "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','content')
        widgets = {
            'content': forms.Textarea(attrs={'style': 'width: 100%; height: 100px;'}),
            # 'name': forms.Textarea(attrs={'style': 'width: 80%; height: 50px;'}),
            # 'email': forms.Textarea(attrs={'style': 'width: 80%; height: 50px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.widget.attrs['class'] = 'form-control required-cls'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name','email','content')
        widgets = {
            'content': forms.Textarea(attrs={'style': 'width: 100%; height: 100px;'}),
            # 'name': forms.Textarea(attrs={'style': 'width: 80%; height: 50px;'}),
            # 'email': forms.Textarea(attrs={'style': 'width: 80%; height: 50px;'}),
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.widget.attrs['class'] = 'form-control required-cls'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
        
        

class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title','description')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email","image","dob","gender","mobile")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email","password","image","dob","gender","mobile")