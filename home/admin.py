from django.contrib import admin

from .models import Article, Image

class ImageImageAdmin(admin.ModelAdmin):
  pass


class ImageImageInline(admin.StackedInline):
  model = Image
  max_num = 10
  extra = 0


class ArticleAdmin(admin.ModelAdmin):
  inlines = [ImageImageInline,]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Image,ImageImageAdmin)