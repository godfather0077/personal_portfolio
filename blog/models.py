from django.db import models
class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    #image=models.ImageField(upload_to='portfolio/images/')
    date=models.DateField()


# Create your models here.
def __str__(self):
    return self.title
