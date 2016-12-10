from django import forms

from .models import Topic, Entry, Booklist


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


class BooklistForm(forms.ModelForm):

    class Meta:
        model = Booklist
        fields = ['booklist_title']
        labels = {'booklist_title': ''}
