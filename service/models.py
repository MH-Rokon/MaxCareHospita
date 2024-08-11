from django.db import models

class service(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField(upload_to="service/image/")
    def __str__(self):
        return self.name