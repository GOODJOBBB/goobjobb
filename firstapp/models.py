from django.db import models

# Create your models here.

class Firstapp(models.Model):
    company = models.CharField('기업이름',max_length=200)
    address = models.CharField('주소', max_length=200)
    pic = models.ImageField("사진", blank=True)
    URL = models.CharField('URL', max_length=200)
    pic = models.ImageField('기업로고', blank=True)
    representative = models.CharField('대표자명', max_length=200)
    telephone = models.CharField("전화번호", max_length=200)
    business = models.CharField("분야", max_length=200)
    volume = models.CharField("모집인원", max_length=200)
    advantage = models.CharField("복리후생", max_length=200)
    type = models.CharField("직종",max_length=200)
    money = models.CharField("급여",max_length=200)
    grade = models.CharField("학력",max_length=200)
    diversification = models.CharField("고용형태",max_length=200)
    career = models.CharField("경력",max_length=200)
    time = models.CharField("근무시간",max_length=200)
    content = models.CharField("직무내용",max_length=200)
    etc = models.TextField("기타사항",max_length=500)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True) #생성될때 픽스됨
    modified_at = models.DateTimeField('수정날짜', auto_now=True)#수정할때마다 바뀜

    def __str__(self):
        return self.title