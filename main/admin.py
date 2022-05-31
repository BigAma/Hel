from django.contrib import admin
from main.models import Category, Professionnel, Demande_client, UserProfil
# Register your models here.

admin.site.register(Category)
admin.site.register(Professionnel)
admin.site.register(Demande_client)
admin.site.register(UserProfil)