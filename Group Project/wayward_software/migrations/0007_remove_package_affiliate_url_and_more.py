# Generated by Django 4.2.5 on 2023-10-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayward_software', '0006_clientprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='affiliate_url',
        ),
        migrations.AddField(
            model_name='package',
            name='subscription_price',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
