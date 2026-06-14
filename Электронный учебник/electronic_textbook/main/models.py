from django.db import models


class Lecture(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название лекции')
    section = models.CharField(max_length=100, verbose_name='Раздел', blank=True)
    content = models.TextField(verbose_name='Текст лекции')
    file = models.FileField(upload_to='lectures/', verbose_name='Файл лекции', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Laboratory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название лабораторной')
    task = models.TextField(verbose_name='Задание')
    code_example = models.TextField(verbose_name='Пример кода', blank=True)
    solution = models.TextField(verbose_name='Решение', blank=True)
    file = models.FileField(upload_to='laboratories/', verbose_name='Файл лабораторной', blank=True, null=True)

    def __str__(self):
        return self.title

class Presentation(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название презентации')
    description = models.TextField(verbose_name='Описание')
    file = models.FileField(upload_to='presentations/', verbose_name='Файл презентации', blank=True, null=True)
    slides_count = models.PositiveIntegerField(default=0, verbose_name='Количество слайдов')

    def __str__(self):
        return self.title


class Material(models.Model):
    FILE_TYPES = [
        ('pdf', 'PDF'),
        ('video', 'Видео'),
        ('ppt', 'Презентация'),
        ('other', 'Другое'),
        ('youtube', 'YouTube'),
        ('image', 'Фото'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название материала')
    file_type = models.CharField(max_length=20, choices=FILE_TYPES, default='pdf', verbose_name='Тип файла')
    youtube_url = models.URLField(max_length=500,blank=True,null=True, verbose_name='YouTube ссылка')
    file = models.FileField(upload_to='materials/', verbose_name='Файл', blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, verbose_name='Размер файла')

    def __str__(self):
        return self.title
class TestQuestion(models.Model):
    question = models.CharField(max_length=300, verbose_name='Вопрос')

    option_a = models.CharField(max_length=200, verbose_name='Вариант A')
    option_b = models.CharField(max_length=200, verbose_name='Вариант B')
    option_c = models.CharField(max_length=200, verbose_name='Вариант C')
    option_d = models.CharField(max_length=200, verbose_name='Вариант D')

    CORRECT_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    correct_answer = models.CharField(
        max_length=1,
        choices=CORRECT_CHOICES,
        verbose_name='Правильный ответ'
    )

    def __str__(self):
        return self.question
    

class GoogleTestForm(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название теста')
    form_url = models.URLField(verbose_name='Ссылка Google Forms')
    is_active = models.BooleanField(default=True, verbose_name='Активный тест')

    def __str__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D')
        ]
    )

    def __str__(self):
        return self.question
    