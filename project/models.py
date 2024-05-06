from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250, verbose_name="Mavzu nomi")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Ilmiy raxbar",
                               help_text="Raxbar kimligini belgilang")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    last_update_time = models.DateTimeField(auto_now=True)
    start_time = models.DateField(verbose_name="Qaysi vaqtdan boshlab talabalar ma'lumot kirita olsin ?")
    end_time = models.DateField(verbose_name="Qachon talabalar ma'lumotlar qo'shisha olishi imkoniyati yopilsin ?")
    slug = models.CharField(max_length=300, unique=True, verbose_name="Slug",
                            help_text="slug qo'yish shart emas o'zi to'ldiradi")
    image = models.ImageField(upload_to="media/", verbose_name="Rasm", help_text="Rasm qo'yish shart")
    body = HTMLField(blank=True, default="", verbose_name="Mazvu haqida to'liq shu yerda yoritib berishingiz mumkin")

    bob1 = models.CharField(max_length=400, verbose_name="1-Bob nomi")

    bob2 = models.CharField(max_length=400, verbose_name="2-Bob nomi")

    bob3 = models.CharField(max_length=400, verbose_name="3-Bob nomi")

    who_can_edit = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='who_can_edit',
                                     verbose_name='Qaysi talaba uchun')

    def __str__(self):
        return self.title[:40]

    def clean(self):
        super().clean()

        if self.start_time == self.end_time:
            raise ValidationError("Boshlanish vaqti va tugash vaqti bir xil bo'lmasiligi shart !")
        elif self.start_time > self.end_time:
            raise ValidationError("Boshlanmasdan oldin tugamasligi kerak ! Vaqtni to'g'ri o'rnating")

    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"


class TeacherArticleCreateNumber(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="Foydalanuvchi",
                                related_name='article_num')
    arcticle_number = models.PositiveIntegerField(default=3, verbose_name="Ushbu o'qituvchi nechta mavzu yarata olsin")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "O'qituvchi mavuzlari soni"
        verbose_name_plural = "O'qituvchi mavuzlari soni"


class Attempt(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    which_task = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.which_task}"