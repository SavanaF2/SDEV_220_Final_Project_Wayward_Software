# Generated by Django 4.2.5 on 2023-09-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayward_software', '0004_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='package_software',
        ),
        migrations.AddField(
            model_name='package',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
