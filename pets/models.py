from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.nome
