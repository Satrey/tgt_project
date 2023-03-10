# Generated by Django 4.1.7 on 2023-02-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_customuser_phone_number_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number_mobile',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Мобильный телефон'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number_work',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Рабочий телефон'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=50, verbose_name='Отдел'),
        ),
    ]
