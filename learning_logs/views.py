from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry, Booklist, Book
from .forms import TopicForm, EntryForm, BooklistForm

# Create your views here.


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    # topic = get_object_or_404(Topic, id=topic_id)
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        if check_topic_owner(request, topic_id):
            form = EntryForm()
        else:
            raise Http404
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        if form.is_valid():
            if check_topic_owner(request, topic_id):
                new_entry.save()
                return HttpResponseRedirect(reverse('learning_logs:topic',
                                                    args=[topic_id]))
            else:
                raise Http404

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    #topic = get_object_or_404(Topic, id=entry.topic.id)
    topic = entry.topic
    topic_id = entry.topic.id

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial rquest; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            if check_topic_owner(request, topic_id):
                form.save()
                return HttpResponseRedirect(reverse('learning_logs:topic',
                                                    args=[topic.id]))
            else:
                raise Http404

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(request, topic_id):
    """get user for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner == request.user:
        return True
    else:
        return False


def search(request):
    """Show search results."""
    if request.method != 'GET':
        raise Http404
    else:
        q = request.GET.get('searchquery', '')
        # api_url = 'http://openlibrary.org/search.json?title=' + q
        context = {'query': q}
        return render(request, 'learning_logs/search.html', context)


@login_required
def booklists(request):
    """Show all booklists"""
    booklists = Booklist.objects.filter(
        owner=request.user).order_by('date_added')
    context = {'booklists': booklists}
    return render(request, 'learning_logs/booklists.html', context)


@login_required
def books(request, booklist_id):
    """Show books for the given Booklist."""
    return render(request, 'learning_logs/index.html')


@login_required
def new_booklist(request):
    """Add a new booklist."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BooklistForm()
    else:
        # POST data submitted; process data.
        form = BooklistForm(request.POST)
        if form.is_valid():
            new_booklist = form.save(commit=False)
            new_booklist.owner = request.user
            new_booklist.save()
            return HttpResponseRedirect(reverse('learning_logs:booklists'))

    context = {'form': form}
    return render(request, 'learning_logs/new_booklist.html', context)
