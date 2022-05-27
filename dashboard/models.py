from django.db import models
from django.urls import reverse
# Create your models here.

DATA_ANIMATION = (
    ('fadeInUp', 'Fade in Up'),
    ('fadeInDown', 'Fade in Down'),
)

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portifolio/covers/', null=True)
    title = models.CharField(max_length=120)
    describ = models.TextField(max_length=256, null=True)
    is_Public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/covers/', null=True)
    title = title = models.CharField(max_length=150)
    title_animation = models.CharField(max_length=15, choices=DATA_ANIMATION, default='fadeInUp')
    title_animation_duration_in = models.CharField(max_length=3, default="0.1")
    subtitle = models.TextField(max_length=500)
    subtitle_animation = models.CharField(max_length=15, choices=DATA_ANIMATION, default='fadeInUp')
    subtitle_animation_duration_in = models.CharField(max_length=3, default="0.5")
    button_name = models.CharField(max_length=32)
    button_link = models.CharField(max_length=128)
    button_animation = models.CharField(max_length=15, choices=DATA_ANIMATION, default='fadeInUp')
    button_animation_duration_in = models.CharField(max_length=3, default="0.8")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class OursClients(models.Model):
    logo = models.ImageField(upload_to='ourClients/logo/', null=True)
    name = models.CharField(max_length=60)
    is_activate = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name