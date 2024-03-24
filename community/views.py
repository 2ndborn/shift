from django.shortcuts import render, reverse, redirect
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

    return render(request, 'community/community.html')


def post(request):
    """A view to return the users post"""
    if request.method == 'POST':
        form = PostForm
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully post!')
            return redirect(reverse('community'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')

    context = {
        'form': form,
    }
    
    return render(request, 'community/community.html', context)
