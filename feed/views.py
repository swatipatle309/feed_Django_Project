
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message, Comment, Like
from .forms import MessageForm, CommentForm

@login_required
def feed(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'feed/feed.html', {'messages': messages})

@login_required
def post_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('feed')
    else:
        form = MessageForm()
    return render(request, 'feed/post_message.html', {'form': form})

@login_required
def post_comment(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.message = message
            comment.save()
            return redirect('feed')
    else:
        form = CommentForm()
    return render(request, 'feed/post_comment.html', {'form': form, 'message': message})

@login_required
def like_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    Like.objects.get_or_create(user=request.user, message=message)
    return redirect('feed')

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    Like.objects.get_or_create(user=request.user, comment=comment)
    return redirect('feed')

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user == message.user:
        message.delete()
    return redirect('feed')

# Create your views here.
