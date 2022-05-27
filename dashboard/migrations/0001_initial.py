# Generated by Django 4.0.4 on 2022-05-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OursClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='ourClients/logo/')),
                ('name', models.CharField(max_length=60)),
                ('is_activate', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='portifolio/covers/')),
                ('title', models.CharField(max_length=120)),
                ('describ', models.TextField(max_length=256)),
                ('is_Public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='slider/covers/')),
                ('title', models.CharField(max_length=150)),
                ('title_animation', models.CharField(choices=[('fadeInUp', 'Fade in Up'), ('fadeInDown', 'Fade in Down')], default='fadeInUp', max_length=15)),
                ('title_animation_duration_in', models.CharField(default='0.1', max_length=3)),
                ('subtitle', models.TextField(max_length=256)),
                ('subtitle_animation', models.CharField(choices=[('fadeInUp', 'Fade in Up'), ('fadeInDown', 'Fade in Down')], default='fadeInUp', max_length=15)),
                ('subtitle_animation_duration_in', models.CharField(default='0.5', max_length=3)),
                ('button_name', models.CharField(max_length=32)),
                ('button_link', models.CharField(max_length=128)),
                ('button_animation', models.CharField(choices=[('fadeInUp', 'Fade in Up'), ('fadeInDown', 'Fade in Down')], default='fadeInUp', max_length=15)),
                ('button_animation_duration_in', models.CharField(default='0.8', max_length=3)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]