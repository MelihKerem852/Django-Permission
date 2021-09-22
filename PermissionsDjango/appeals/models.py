from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
STATES = [
    ('','Seçiniz...'),
    ('Lise','Lise'),
    ('Üniversite','Üniversite'),
    ('Yüksek Lisans','Yüksek Lisans')
]
DEFAULT_STATUS = "Bilinmiyor"
STATUS = [
    ('','Seçiniz...'),
    ('Stajyer','Stajyer'),
    ('Tecrübesiz','Tecrübesiz'),
    ('Orta Tecrübeli','Orta Tecrübeli'),
    ('Tecrübeli','Tecrübeli'),
]
DEFAULT_DEPARTMENT = "Bilinmiyor"
DEPARTMENT = [
    ('','Seçiniz...'),
    ('Yazılım','Yazılım'),
    ('Halkla İlişkiler','Halkla İlişkiler'),
    ('Stajyer','Stajyer'),
    ('Web Tasarım','Web Tasarım'),
    ('Tasarımcı','Tasarımcı'),
]

class Appeal(models.Model):
    name = models.CharField(max_length=200,verbose_name="İsim")
    last_name = models.CharField(max_length=200,verbose_name="Soy İsim")
    email = models.EmailField(verbose_name="E-mail")
    age = models.CharField(verbose_name="Yaş",max_length=30)
    education = models.CharField(
        choices=STATES,
        max_length=80,
        verbose_name="Eğitim Seviyesi"
    )
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=200,
        verbose_name="Statü"
    )
    department = models.CharField(
        default=DEFAULT_DEPARTMENT,
        choices=DEPARTMENT,
        max_length=200,
        verbose_name="Departman"
    )
    company = models.ForeignKey('company.Company',related_name='appeals',on_delete=CASCADE)
    about = models.TextField(verbose_name="Hakkınızda")
    appeal_date = models.DateTimeField(auto_now_add=True,verbose_name="Başvuru Tarihi")
    cv = models.FileField(upload_to="CVs",blank=True,null=True,verbose_name="CV Ekleyin: ")