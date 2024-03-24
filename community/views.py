from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .models import Post
from .forms import PostForm


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

    context = {
        'post_list': posts,
    }

    return render(request, 'community/community.html', context)


def post(request):
    """A view to return the users post"""
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


