from django.db import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField('Название статьи ', max_length=200)
    article_text = models.TextField('текст')
    pub_date = models.DateTimeField('дата')
    img_post = models.ImageField("Изображение", upload_to="img")
    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("Изображение", upload_to="img")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'