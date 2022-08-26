from ast import Sub
from site import USER_BASE
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.
class Subscribe(models.Model):
    class USER_TYPE(models.TextChoices):
        Bronz = 'BR', 'Bronz'
        Gold = 'GD', 'Gold'
        Platinum = 'PL', 'Platinum'
        PlatinumPlus = 'PP', 'Platinum Plus'
        free = 'FR', 'Bedavaci'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subsribe')
    type = models.CharField(max_length=2, choices=USER_TYPE.choices, default=USER_TYPE.free)

    def __str__(self):
        return self.user.username

    def get_badge_url(self):
        if self.type == Subscribe.USER_TYPE.Bronz:
            return static('bronz.png')
        elif self.type == Subscribe.USER_TYPE.Gold:
            return static('gold.png')
        elif self.type == Subscribe.USER_TYPE.Platinum:
            return static('platinum.png')
        elif self.type == Subscribe.USER_TYPE.PlatinumPlus:
            return static('platinum-plus.png')
        else:
            return static('free.png')