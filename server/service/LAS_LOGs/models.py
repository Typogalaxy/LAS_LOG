from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """留言"""

    topic = models.ForeignKey(Topic, models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."


class Link(models.Model):
    """链接页面"""

    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Work(models.Model):
    """链接页面"""

    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title
