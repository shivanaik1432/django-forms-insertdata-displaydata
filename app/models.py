from django.db import models

# Create your models here.
class Membership(models.Model):
    package=models.CharField(max_length=10)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.package)
