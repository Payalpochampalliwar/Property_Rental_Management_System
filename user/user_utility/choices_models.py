from django.db import models
class UserGender(models.TextChoices):
    MALE = "M", 
    FEMALE = "F"