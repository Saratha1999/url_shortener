from django.db import models
import string  #python libraries
import random

# Create your models here.

def generate_short_code():
    #Generates a random 6-character short code
    return ''.join(random.choices(string.ascii_letters+string.digits, k = 6))


class Shortened_URL(models.Model):

    original_url = models.URLField(unique=True) #store original long URL
    short_code = models.CharField(max_length=6, unique= True, default= generate_short_code) ## Unique short code

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"