# Generated by Django 4.0.4 on 2022-05-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_portifolio_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='describ',
            field=models.TextField(max_length=256, null=True),
        ),
    ]
