
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

class User(AbstractUser):
    pass
    image = models.ImageField(upload_to='Images/')
    dob = models.DateField('DOB', null=True, blank=True)
    gender_choices =(('male','MALE'),
                     ('female','FEMALE'),
                     ('other','OTHER'))
    gender = models.CharField(max_length=7, choices=gender_choices)
    
    mobile = models.CharField('Mobile', max_length=50)

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='extends',null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='Images/thumbnails/',null=True, blank=True)
    main_image = models.ImageField(upload_to='Images/mainimage/', null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title     

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    content = models.TextField('Comment')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author_email} - {self.content[:60]}' 

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author_email} - {self.content[:60]}'
    