from django.shortcuts import render
from .models import DefaultTopicTag, DefaultUserTag, DefaultWorkTag
from django.contrib.auth.decorators import login_required


@login_required()
def edit_topic_tag(request, topic_id):
    """显示所有默认主题标签 show all topic tags"""
    all_default_topic_tags = DefaultTopicTag.objects.order_by('id')
    context = {'default_tags': all_default_topic_tags}
    return render(request, 'tags/edit_tag.html', context)


@login_required()
def edit_user_tag(request, user_id):
    """显示所有默认用户标签 show all user tags"""
    all_default_user_tags = DefaultUserTag.objects.order_by('id')
    context = {'default_tags': all_default_user_tags}
    return render(request, 'tags/edit_tag.html', context)


@login_required()
def edit_work_tag(request, work_id):
    """显示所有默认作品标签 show all work tags"""
    all_default_work_tags = DefaultWorkTag.objects.order_by('id')
    context = {'default_tags': all_default_work_tags}
    return render(request, 'tags/edit_tag.html', context)
