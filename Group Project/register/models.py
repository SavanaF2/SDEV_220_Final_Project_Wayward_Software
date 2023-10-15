from django.db import models
from django.contrib.auth.models import  Group, Permission
from django.contrib.auth.models import User 

from django.db.models.signals import post_save #add this

class employeeProfile(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this employee belongs to. A user will get all permissions granted to each of their groups.',
        related_name='employee_users_groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this employee.',
        verbose_name='user permissions',
        related_name='employee_users_permissions',
    )
