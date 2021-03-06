from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.CharField(max_length=30, unique=True, verbose_name='id')
    user_pw = models.CharField(max_length=100, verbose_name='password')
    user_name = models.CharField(max_length=20, unique=True, verbose_name='name')
    user_email = models.EmailField(max_length=150, unique=True, verbose_name='email')
    NATIONAL_CHOICES = (
        ('TY', '태양인'),
        ('TE', '태음인'),
        ('SY', '소양인'),
        ('SE', '소음인')
    )
    nationality = models.CharField(max_length=2, null=True, choices=NATIONAL_CHOICES, verbose_name='nationality')
    def __str__(self):
        return self.user_name
    
    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'