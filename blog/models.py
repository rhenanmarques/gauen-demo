
from django.db import models
from django.contrib.auth.models import User
from slug import slug
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=160, unique=True)
    slug = models.SlugField(max_length=160, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slug(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=160)
    slug = models.SlugField(unique=True, max_length=160)
    article = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='blog/covers/', null=True)
    cover_describ = models.CharField(max_length=160, default="post-image")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = slug(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title