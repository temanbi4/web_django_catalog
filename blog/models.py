from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField
class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    slug = AutoSlugField(populate_from='title', unique=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_post_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
