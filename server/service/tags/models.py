from django.db import models


class Tag(models.Model):
    """标签"""
    text = models.CharField(max_length=200)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
