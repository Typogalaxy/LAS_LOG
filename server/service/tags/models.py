from django.db import models
from server.service.LAS_LOGs.models import Topic


class Tag(models.Model):
    """标签"""
    topic = models.ForeignKey(Topic, models.CASCADE)
    text = models.CharField(max_length=200, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
