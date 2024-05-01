from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='_profile_images')
    contact_number = models.CharField(blank=True, max_length=20)

    def __str__(self) -> str:
        if self.contact_number:
            return f"{self.user.username} - {self.contact_number}"
        else:
            return f"{self.user.username}"

