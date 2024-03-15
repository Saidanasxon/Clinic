from django.contrib import admin
from .models import User,Doktor,QabulVaqti,Davolash
# Register your models here.



@admin.register(Doktor)

class DoktorAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'soha', 'rasmi')


@admin.register(QabulVaqti)

class QabulVaqtiadmin(admin.ModelAdmin):
    list_display = ('id', 'doktor',  'band')

@admin.register(Davolash)

class Davolashadmin(admin.ModelAdmin):
    list_display = ('id', 'foydalanuvchi', 'qabul_vaqt')