from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User

# Create your models here.

class Treiner(models.Model):
    f_name = models.CharField(
        max_length=80,
        verbose_name="F.I.SH",
        null=True, blank=True
    )
    professional = models.CharField(
        max_length=150,
        verbose_name="Yonalishi",
        null=True, blank=True
    )
    img = models.ImageField(
        default="default/user.png",
        upload_to="trainers/img/%Y-%m-%d",
        verbose_name="Foto"
    )
    order_num = models.IntegerField(default=0)
    about = QuillField(null=True, blank=True, verbose_name="Muraibiy xaqida")
    instagram = models.URLField(verbose_name="Instagram URL", null=True, blank=True)
    facebook = models.URLField(verbose_name="Facebook URL", null=True, blank=True)
    telegram = models.URLField(verbose_name="Telegram URL", null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = ''
        managed = True
        ordering = ["order_num"]
        verbose_name = 'Trainerlar'
        verbose_name_plural = 'Trainerlar'


    def __str__(self):
        return f"{self.f_name}"    



class Times(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    come_time = models.TimeField(null=True, blank=True, verbose_name="Kelish vaqti")
    left_time = models.TimeField(null=True, blank=True, verbose_name="Ketish vaqti")
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.come_time} {self.left_time}"
    


class Weeks(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=12, verbose_name="Nomi", help_text="'Dushanba' vhz...")
    time = models.ManyToManyField(Times, related_name="Times")
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"



class Contact(models.Model):
    """ CONTACT """
    f_name = models.CharField(max_length=100, verbose_name="F.I.SH", null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name="Telefon raqam", null=True, blank=True)
    text = models.TextField(null=True, blank=True, verbose_name="Message")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Xat kelgan vaqt")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Xat o'qilgan vaqt")


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Xatlar'
        verbose_name_plural = 'Xatlar'


    def __str__(self):
        return f"{self.f_name} {self.add_time}"
    


class Member(models.Model):
    "A'zo  BOLMOQCHI odamlar"
    f_name = models.CharField(max_length=100, verbose_name="F.I.SH", null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name="Telefon raqam", null=True, blank=True)
    text = models.TextField(null=True, blank=True, verbose_name="Message")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Xat kelgan vaqt")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Xat o'qilgan vaqt")


    class Meta:
        db_table = ''
        managed = True
        verbose_name = "A'zolik uchun xat"
        verbose_name_plural = "A'zolik uchun xat"


    def __str__(self):
        return f"{self.f_name} {self.add_time}"


    
    