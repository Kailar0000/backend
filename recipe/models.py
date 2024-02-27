from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model


User = get_user_model()

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Name:{self.name}'


class Recipes(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    short_description = models.TextField(verbose_name='Краткое описание', max_length=500)
    time = models.TextField(verbose_name='Время готовки', max_length=50)
    category = models.ForeignKey(to=Categories, verbose_name='Катигория', on_delete=models.CASCADE)
    ingredients = models.TextField(verbose_name='Ингридиенты', max_length=500)
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts', default=1)
    description = models.TextField()
    steps = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    thumbnail = models.ImageField(
        verbose_name='Превью рецепта',
        blank=True,
        upload_to='images/thumbnails/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )

    class Meta:
        ordering = ['-time_create']
        indexes = [models.Index(fields=['-time_create'])]
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_absolute_url(self):
        return reverse('recipe_page', kwargs={'recipe_pk': self.slug})

    def __str__(self):
        return self.title
