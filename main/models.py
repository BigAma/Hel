from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserProfil(models.Model):
    user_profil = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    user_username = models.CharField(max_length=100, null=True)
    user_nom = models.CharField(max_length=100, null=True)
    user_prenom = models.CharField(max_length=100, null=True)
    user_adresse = models.CharField(max_length=150, null=True)
    user_email = models.EmailField(unique=True, null=True)
    user_tel = models.IntegerField(unique=True, null=True)
    user_isPro = models.BooleanField(default=False)

    def __str__(self):
        return self.user_username

    def isPro(self):
        self.user_isPro = True
        self.save()



class Category(models.Model):
    category_name = models.CharField(max_length=150)
    category_description = models.TextField()
    category_img = models.ImageField(null=True, default="cat.svg", upload_to='upload/')

    def __str__(self):
        return self.category_name


class Professionnel(models.Model):
    pro_name = models.CharField(max_length=150)
    pro_description = models.TextField()
    pro_img = models.ImageField(null=True, default="avatar.svg", upload_to='upload/')
    pro_rate = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    pro_category = models.ManyToManyField(Category)

    def __str__(self):
        return self.pro_name


class Demande_client(models.Model):
    demande_sujet = models.CharField(max_length=100, null=True)
    demande_description = models.TextField(null=True)
    demande_modification = models.DateField(auto_now=True, null=True)
    demande_creation = models.DateField(auto_now_add=True, null=True)
    demande_utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    demande_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    demande_datevoulue = models.DateField(auto_now=True, null=True)
    demande_onGoing = models.BooleanField(default="True", null=True, blank=True)

    def __str__(self):
        return self.demande_sujet
