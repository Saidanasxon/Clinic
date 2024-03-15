from django.db import models
from django.contrib.auth.models import User

class Doktor(models.Model):
    id = models.AutoField(primary_key=True)
    ism = models.CharField(max_length=50)
    soha = models.CharField(max_length=50)
    rasmi = models.ImageField(upload_to='doktor')

    def __str__(self) -> str:
        return self.ism

class QabulVaqti(models.Model):
    id = models.AutoField(primary_key=True)
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE, related_name='qabul_vaqt')
    vaqt = models.CharField(max_length=50)
    band=models.BooleanField(default=False)
    
class Davolash(models.Model):
    id = models.AutoField(primary_key=True)
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE)
    qabul_vaqt = models.ForeignKey(QabulVaqti, on_delete=models.CASCADE)

