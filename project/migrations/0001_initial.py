# Generated by Django 4.2.6 on 2023-11-13 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(help_text='masalan: KIF', max_length=250, unique=True, verbose_name='Gurux nomi')),
                ('student_list', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name="Talabalar ro'yxati. Bir nechtasini tanlash uchun ctrl ni bosib turgan holatda belgilang")),
            ],
            options={
                'verbose_name': 'Gurux nomi',
                'verbose_name_plural': 'Gurux nomi',
            },
        ),
        migrations.CreateModel(
            name='TeacherArticleCreateNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arcticle_number', models.PositiveIntegerField(default=3, verbose_name="Ushbu o'qituvchi nechta mavzu yarata olsin")),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': "O'qituvchi mavuzlari soni",
                'verbose_name_plural': "O'qituvchi mavuzlari soni",
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Mavzu nomi')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateField(verbose_name="Qaysi vaqtdan boshlab talabalar ma'lumot kirita olsin ?")),
                ('end_time', models.DateField(verbose_name="Qachon talabalar ma'lumotlar qo'shisha olishi imkoniyati yopilsin ?")),
                ('slug', models.CharField(help_text="slug qo'yish shart emas o'zi to'ldiradi", max_length=300, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(help_text="Rasm qo'yish shart", upload_to='media/', verbose_name='Rasm')),
                ('body', tinymce.models.HTMLField(blank=True, default='', verbose_name="Mazvu haqida to'liq shu yerda yoritib berishingiz mumkin")),
                ('bob1', models.CharField(max_length=400, verbose_name='1-Bob nomi')),
                ('bob1_1', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob1_2', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob1_3', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob2', models.CharField(max_length=400, verbose_name='2-Bob nomi')),
                ('bob2_1', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob2_2', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob2_3', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob3', models.CharField(max_length=400, verbose_name='3-Bob nomi')),
                ('bob3_1', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob3_2', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('bob3_3', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('author', models.ForeignKey(help_text='Raxbar kimligini belgilang', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ilmiy raxbar')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.groupname', verbose_name="Qaysi gurux ushbu mavzuni ko'rishi yoki tahrirlashi mumkin")),
            ],
            options={
                'verbose_name': 'Mavzu',
                'verbose_name_plural': 'Mavzular',
            },
        ),
    ]
