from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def paginate_page(queryset, request):
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
    }


def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    context = paginate_page(posts, request)
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    context = {
        'group': group,
        'posts': posts,
    }
    context.update(paginate_page(posts, request))
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author).order_by('-pub_date')
    count_posts = posts.count()
    context = {
        "author": author,
        "count_posts": count_posts,
    }
    context.update(paginate_page(posts, request))
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = post.author
    count_posts = author.posts.count()
    context = {
        "post": post,
        "count_posts": count_posts,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('posts:profile', username=request.user)
    form = PostForm()
    groups = Group.objects.all()
    context = {
        "form": form,
        "groups": groups,
    }
    return render(request, "posts/create_post.html", context)


@login_required
def post_edit(request, post_id):
    is_edit = True
    post = get_object_or_404(Post, pk=post_id)
    groups = Group.objects.all()
    form = PostForm(request.POST or None, instance=post)
    if request.user != post.author:
        return redirect("posts:profile", post.author)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post.id)
    context = {
        "form": form,
        "is_edit": is_edit,
        "post": post,
        "groups": groups,
    }
    return render(request, "posts/create_post.html", context)
