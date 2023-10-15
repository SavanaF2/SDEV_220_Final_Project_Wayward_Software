from django.conf import settings
from django.db import models
from django.utils import timezone
from django.dispatch import receiver #add this
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save #add this
    

#class for software options
class Package(models.Model):
    package_name = models.CharField(max_length=150, unique = True)
    description = models.CharField(max_length=300, null=True)
    subscription_price = models.CharField(max_length=4, null=True)
    surrogate_key = models.IntegerField( unique=True, null=True)

# Create your models here.
#connects a profile to a client
class clientProfile(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    packages = models.ManyToManyField(Package)

#automatically adds a profile when a client is created and saves when a client is saved
    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            clientProfile.objects.create(client=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.clientprofile.save()

