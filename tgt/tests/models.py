from django.db import models


class Theme(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Тема')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='theme')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы тестов'

    def __str__(self):
        return self.title


class Ticket(models.Model):
    title = models.CharField(max_length=20, db_index=True, verbose_name='Билет')
    slug = models.SlugField(max_length=25, db_index=True, verbose_name='ticket')
    theme = models.ForeignKey('Theme', default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.TextField(max_length=400, verbose_name='Вопрос')
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title[:15]


class Answer(models.Model):
    questionId = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    IsRight = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text



