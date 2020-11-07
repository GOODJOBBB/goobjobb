from django.db import models

# Create your models here.

class Firstapp(models.Model):
    company = models.CharField('기업이름',max_length=200)
    address = models.CharField('주소', max_length=200)
    URL = models.CharField('URL', max_length=200)
    desc = models.TextField('본문',blank=True)
    pic = models.ImageField('기업로고', blank=True)
    representative = models.CharField('대표자명', max_length=200)
    telephone = models.CharField("전화번호", max_length=200)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True) #생성될때 픽스됨
    modified_at = models.DateTimeField('수정날짜', auto_now=True)#수정할때마다 바뀜

    def __str__(self):
        return self.title