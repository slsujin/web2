from django.db import models

# Create your models here.
class travel1(models.Model):
    name= models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.name