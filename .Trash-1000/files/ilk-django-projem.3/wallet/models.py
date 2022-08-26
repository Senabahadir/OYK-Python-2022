from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cuzdan(models.Model):
    class PARA_BIRIMLERI(models.TextChoices):
        USD = 'USD', 'Dolar'
        EUR = 'EUR', 'Euro'
        TL = 'TL', 'Turk Lirasi'
        BTC = 'BTC', 'Bitcoin'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cuzdanlar')
    para_birimi = models.CharField(max_length=3, choices=PARA_BIRIMLERI.choices,
        default=PARA_BIRIMLERI.TL)
    bakiye = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('user', 'para_birimi',)

    def __str__(self):
        return self.user.first_name + ': ' + str(self.bakiye) + self.para_birimi