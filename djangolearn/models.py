from django.db import models


# Create your models here.

class sinfdoshlar(models.Model):
    firstname = models.CharField(null=False, max_length=20)
    lastname = models.CharField(null=False, max_length=20)

    class Meta:
        verbose_name_plural = "sinfdoshlar"

    def __str__(self):
        return self.firstname
