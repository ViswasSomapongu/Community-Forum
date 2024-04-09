from django.shortcuts import render, redirect,get_object_or_404
from .forms import ThreadForm, ReplyForm
from .models import Thread, Reply

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ThreadForm()
    threads = Thread.objects.order_by('-date_created')
    return render(request, 'forumapp/index.html',{'form':form, 'threads':threads})


def thread(request, thread_id):
    the_thread = Thread.objects.get(pk=thread_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = the_thread
            reply.user = request.user
            reply.save()
            return redirect('thread', thread_id=the_thread.id)

    else:
        form = ReplyForm()
    return render(request, 'forumapp/thread.html',{'form':form, 'thread':the_thread})

def delete_reply(request, reply_id):
    if request.method == 'POST':
        reply = get_object_or_404(Reply, pk=reply_id)
        # Check if the current user is the author of the reply
        if request.user == reply.user:
            reply.delete()
    # Redirect back to the thread after deletion
    return redirect('thread', thread_id=reply.thread.id)

