from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# models.py
class User(AbstractUser):
    # username = models.CharField("사용자 계정", max_length=20, unique=True)
    username = models.CharField("사용자 계정", max_length=50, unique=True)
    # email = models.EmailField("이메일 주소", max_length=100, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    # password = models.CharField("비밀번호", max_length=60)
    password = models.CharField("비밀번호", max_length=60)
    # fullname = models.CharField("이름", max_length=20)
    fullname = models.CharField("이름", max_length=20)
    # join_date = models.DateTimeField("가입일", auto_now_add=True)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    user_rank = models.IntegerField("회원등급",default=0)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    # user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="사용자", on_delete=models.CASCADE)
    # hobby = models.ManyToManyField(to="Hobby", verbose_name="취미")
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미")
    # introduction = models.TextField("소개")
    introduction = models.TextField("소개")
    # birthday = models.DateField("생일")
    birthday = models.DateField("생일")
    # age = models.IntegerField("나이")
    age = models.IntegerField("나이")

    def __str__(self):
        return self.user


class Hobby(models.Model):
    # name = models.CharField("취미", max_length=50)
    name = models.CharField("취미", max_length=50)

    def __str__(self):
        return self.name
