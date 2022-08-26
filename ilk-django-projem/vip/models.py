from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscribe(models.Model):
    class USER_TYPE(models.TextChoices):
        Bronz = 'BR', 'Bronz'
        Gold = 'GD', 'Gold'
        Platinum = 'PL', 'Platinum'
        PlatinumPlus = 'PP', 'Platinum Plus'
        free = 'FR', 'Bedavaci'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='izinler')
    type = models.CharField(max_length=2, choices=USER_TYPE.choices, default=USER_TYPE.free)

    def __str__(self):
        return self.user.username
