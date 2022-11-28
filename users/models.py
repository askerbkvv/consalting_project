from django.contrib.auth.models import User
from django.db import models


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Form(models.Model):
    name = models.CharField("Имя", max_length=50, null=True)
    last_name = models.CharField("Фамилия", max_length=60, blank=True)
    phone = models.CharField("Номер телефона", max_length=20, null=True)
    email = models.EmailField("Электронный адрес", max_length=150, null=True)
    content = models.TextField("Вопросы", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Form")
        verbose_name_plural = ("Forms")


class Comment(models.Model):
    name = models.CharField("Имя", max_length=60, null=True)
    last_name = models.CharField("Фамилия", max_length=60, null=True)
    description = models.TextField("Описание", max_length=222, blank=True)
    img = models.ImageField("Фото студента", upload_to="images/students/", null=True)
    country = models.CharField("Куда поступил", max_length=222, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")


class University(models.Model):
    title = models.CharField("Название", max_length=50, null=True)
    img = models.ImageField("Фото университета", upload_to="images/university/", null=True)
    country = models.CharField("Место положение", max_length=222, null=True)
    link = models.CharField("Ссылка сайта университета", max_length=300, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("University")
        verbose_name_plural = ("Universities")



