from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic, Entry, Book, Booklist

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Booklist)
admin.site.register(Book)
