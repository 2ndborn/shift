from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by(-created_on)

        context = {
            'post_list': posts,
        }

        return render(request, 'community/community.html', context)

def community(request):
    """A view to return the community page""" 
    posts = Post.objects.all()
    comments = Comment.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "User doesn't exist")
                return redirect(reverse('community'))

            queries = Q(member__username__icontains=query)
            posts = posts.filter(queries)

    context = {
        'post_list': posts,
        'comment_list': comments,
        'search_term': query
    }

    return render(request, 'community/community.html', context)


def post(request):
    """A view to return the users post"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))   
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.member = request.user
            post.save()
            messages.success(request, 'Successfully post!')
            return redirect(reverse('community'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'community/post.html', context)


def edit_post(request, post_id):
    """A view to edit the users post"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))   
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('community'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)

    template = 'community/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_post(request, post_id):
    """A view to delete the users post"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))   
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('community'))


def comment(request, post_id):
    """A view to comment another users post"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))   
    post = get_object_or_404(Post, pk=post_id)
    comment_instance = None

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment_instance)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = request.user
            comment.post = post
            comment.save()
            form.save()
            messages.success(request, 'Successfully posted a comment!')
            return redirect(reverse('community'))
        else:
            messages.error(request, 'Failed to post comment. Please ensure the form is valid.')
    else:
        form = CommentForm(instance=comment_instance)

    template = 'community/comment.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def edit_comment(request, post_id, comment_id):
    """A view to edit comments"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))   
    post = get_object_or_404(Post, pk=post_id)
    comment_instance = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment_instance)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = request.user
            comment.post = post
            comment.save()
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('community'))
        else:
            messages.error(request, 'Failed to post comment. Please ensure the form is valid.')
    else:
        form = CommentForm(instance=comment_instance)

    template = 'community/edit_comment.html'
    context = {
        'form': form,
        'post': post,
        'comment': comment_instance,
    }

    return render(request, template, context)


def delete_comment(request, post_id, comment_id):
    """A view to delete a comment"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))   
    post = get_object_or_404(Post, pk=post_id)
    comment_instance = get_object_or_404(Comment, pk=comment_id)
    comment_instance.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('community'))