"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Page for adding a new topic.
    url(r'^newtopic/$', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$',
        views.edit_entry, name='edit_entry'),

    # Page for displaying search results.
    url(r'^search/$', views.search, name='search'),

    # Show all booklists.
    url(r'^booklists/', views.booklists, name='booklists'),

    # Detail page for a single booklist
    url(r'^booklists/(?P<booklist_id>\d+)/$', views.books, name='books'),

    # Page for adding a new booklist.
    url(r'^newbooklist/$', views.new_booklist, name='new_booklist'),

    # Show all books.
    #url(r'^books/(?P<book_id>\d+)/$', views.books, name='books'),
]
