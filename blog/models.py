# _*_ encoding:utf-8 _*_
import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags

# Create your models here.


class CateGory(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"文章分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=70, verbose_name=u"文章标签")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70, verbose_name=u"文章标题")

    # 文章正文
    body = models.TextField(verbose_name=u"正文")
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True, verbose_name=u"摘要")

    # 创建时间和修改时间
    created_time = models.DateTimeField(verbose_name=u"创建时间")
    modified_time = models.DateTimeField(verbose_name=u"修改时间")

    # 外键 和文章分类、tag连接
    category = models.ForeignKey(CateGory, verbose_name=u"分类")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u"标签")

    # 文章作者
    author = models.ForeignKey(User, verbose_name=u"作者")

    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0, verbose_name=u"阅读量")

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
        verbose_name = u"文章正本"
        verbose_name_plural = verbose_name


