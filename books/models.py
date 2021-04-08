from django.db import models

# Create your models here.
class Book(models.Model):
    name                =                       models.CharField(max_length=100)
    icon                =                       models.FileField( upload_to='icons/', blank=True, )
    description         =                       models.CharField(max_length=1000)
    book                =                       models.FileField(null = True,upload_to='books/')
