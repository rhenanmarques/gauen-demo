# Generated by Django 4.0.4 on 2022-05-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauenPublic', '0002_alter_price_utilization'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefulLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128)),
                ('url', models.URLField()),
            ],
        ),
    ]
