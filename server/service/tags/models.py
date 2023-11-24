from django.db import models
from server.service.LAS_LOGs.models import Topic, Work
from django.contrib.auth.models import User


class TopicTag(models.Model):
    """标签"""
    topic = models.ForeignKey(Topic, models.CASCADE)
    text = models.CharField(max_length=200, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class DefaultTopicTag(models.Model):
    text = models.CharField(max_length=200, default="")

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class UserTag(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    text = models.CharField(max_length=200, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class DefaultUserTag(models.Model):
    text = models.CharField(max_length=200, default="")

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class WorkTag(models.Model):
    user = models.ForeignKey(Work, models.CASCADE)
    text = models.CharField(max_length=200, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class DefaultWorkTag(models.Model):
    text = models.CharField(max_length=200, default="")

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
