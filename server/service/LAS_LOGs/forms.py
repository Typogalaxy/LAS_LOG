from django import forms
from .models import Topic, Entry, Link


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['text']
        labels = {'text': ''}
