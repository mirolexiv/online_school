from django.db import models

# Create your models here.

class Students(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Прізвище')
    first_name = models.CharField(max_length=100, verbose_name= 'Ім\'я')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name='Побатькові')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата народження')
    grade = models.IntegerField(verbose_name= 'Клас')

    class Meta:
        verbose_name = 'Учень'
        verbose_name_plural = 'Учень'

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic


class Teachers(models.Model):
    last_name = models.CharField(max_length=100,verbose_name='Прізвище')
    first_name = models.CharField(max_length=100, verbose_name= 'Ім\'я')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name='Побатькові')
    subject = models.CharField(max_length=100, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Вчитель'
        verbose_name_plural = 'Вчитель'

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic

class Subjects(models.Model):
    name = models.CharField(max_length=100, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмет'

    def __str__(self):
        return self.name

class Lessons(models.Model):
    student = models.ForeignKey(Students, on_delete=models.PROTECT, verbose_name="Учень")
    teacher = models.ForeignKey(Teachers, on_delete=models.PROTECT, verbose_name="Вчитель")
    data = models.DateField(verbose_name='Дата уроку')
    subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, verbose_name='Навчальний предмет')
    duration = models.IntegerField(verbose_name='Тривалість')

    class Meta:
        verbose_name = 'Заняття'
        verbose_name_plural = 'Заняття'

    def __str__(self):
        return str(f'Учень {self.student}. Вчитель {self.teacher}. Предмет {self.subject}. Дата {self.data}')