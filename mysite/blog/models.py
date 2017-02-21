from django.db import models
from django.contrib import admin


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, verbose_name='blog')
    name = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(User)
admin.site.register(Comment)
