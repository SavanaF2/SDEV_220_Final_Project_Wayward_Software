# Generated by Django 4.2.5 on 2023-09-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayward_software', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_name', models.CharField(max_length=150)),
                ('software_type', models.CharField(max_length=25)),
                ('software_description', models.TextField(max_length=3)),
                ('affiliate_url', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
