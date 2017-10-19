# _*_ coding: utf-8 _*_
from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"名字")
    email = models.EmailField(max_length=255, verbose_name=u"邮箱")
    url = models.URLField(blank=True, verbose_name=u"个人网站")
    text = models.TextField(verbose_name=u"评论内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u"评论当前时间")

    post = models.ForeignKey('blog.Post', verbose_name=u"评论的文章")

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name

