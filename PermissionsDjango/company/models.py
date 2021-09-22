from django.db import models

# Create your models here.
class Company(models.Model):
    image = models.ImageField(blank=True,null=True,verbose_name="Kart Fotoğrafı Ekleyin: ",upload_to="media")
    title = models.CharField(max_length=50,null=False,blank=False,verbose_name="Kart Başlığı: ")
    content = models.TextField(max_length=220,null=False,blank= False, verbose_name="İçerik")
    location = models.CharField(max_length=100,null=False,blank=False,verbose_name="Lokasyon")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.title
    class Meta:
        ordering= ['-created_date'] 