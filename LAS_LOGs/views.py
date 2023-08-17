from django.shortcuts import render
from .models import Topic, Entry, Link
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm, LinkForm
from django.contrib.auth.decorators import login_required


def index(request):
    """LAS记事本的主页 LAS_LOG mian page"""
    return render(request, 'LAS_LOG/index.html')


@login_required
def topics(request):
    """显示所有主题 show all topics"""
    all_topic = Topic.objects.order_by('date_added')
    context = {'topics': all_topic}
    return render(request, 'LAS_LOG/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic_specific = Topic.objects.get(id=topic_id)
    entries = topic_specific.entry_set.order_by('-date_added')
    context = {'topic': topic_specific, 'entries': entries}
    return render(request, 'LAS_LOG/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LAS_LOGs:topics'))
    context = {'form': form}
    return render(request, 'LAS_LOG/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('LAS_LOGs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'LAS_LOG/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LAS_LOGs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'LAS_LOG/edit_entry.html', context)


@login_required
def links(request):
    all_link = Link.objects.order_by('date_added')
    context = {'links': all_link}
    return render(request, 'LAS_LOG/links.html', context)


@login_required()
def new_link(request):
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = LinkForm()
    else:
        # POST提交的数据,对数据进行处理
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LAS_LOGs:links'))
    context = {'form': form}
    return render(request, 'LAS_LOG/new_link.html', context)
