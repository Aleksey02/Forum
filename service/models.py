from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(verbose_name='название', max_length=100)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='картинка', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('index')


class Coment(models.Model):
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    post = models.ForeignKey(Post, related_name='coments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description}'
    def get_absolute_url(self):
        return reverse('index')
