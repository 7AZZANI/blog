from django.shortcuts import render, get_object_or_404 , redirect
from .models import Post  
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        "posts" : posts
    }
    return render(request, 'blog/post_list.html', context)

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context  =  {
        "post" : post
    }
    return render(request, 'blog/details.html', context)


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.published_date = timezone.now()
            form.save()
            return redirect('new_post', pk=post.pk)  # Replace 'post_list' with the URL or name of your post list view
    else:
        form = PostForm()
    
    context = {
        "form": form
    }
    return render(request, 'blog/new_post.html', context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.published_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else :
        form = PostForm(instance=post)
    context = {
        "form" : form,
        "post" : post
    }    
    return render(request, 'blog/new_post.html', context)    