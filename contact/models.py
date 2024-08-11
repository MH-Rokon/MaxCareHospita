from django.db import models

class Contact(models.Model):
    hospital_name = models.CharField(max_length=200,blank=True,null=True)
    hospital_short_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    location_image = models.ImageField(upload_to='contacts/media/uploads/', blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    contact_time = models.CharField(max_length=100, blank=True, null=True) 

    
    def __str__(self):
        return f"{self.hospital_name} ({self.hospital_short_name})"
