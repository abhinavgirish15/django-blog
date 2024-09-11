from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import authenticate
from .models import User
from .models import Category
from .forms import CatForm
from .forms import TagForm
from .models import Tag
from .models import Comment
from .models import Reply
from .forms import CommentForm
from .forms import ReplyForm

def jquery(request):
    return render(request, 'blog/jquery.html')

def addcategory(request):
    if request.method == 'POST':

        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcategory')
        
    else:
        form = CatForm()
    return render(request, 'blog/addcategory.html', {'form': form})

def addtag(request):
    if request.method == "POST":
        
        tagform = TagForm(request.POST)
        if tagform.is_valid():

            tagform.save()
            return redirect('addtag')
    else:
        tagform = TagForm()
    return render(request, 'blog/addtag.html', {'tagform': tagform})



def cat_list(request):
    cats = Category.objects.all()
    print(cats)
    return render(request, 'blog/categorylist.html', {'cats': cats})

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/categoryfilter.html', {'category': category, 'posts': posts})

def tag_list(request):
    tags = Tag.objects.all()
    print(tags)
    return render(request, 'blog/taglist.html', {'tags': tags})
    
def tag_view(request, slug):
    tags = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tags)
    return render(request, 'blog/tagfilter.html', {'tags': tags, 'posts': posts})    


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def commentsection(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                # comment.author_email = request.user.email
                # comment.name = request.user.get_full_name
                comment.save()
                return redirect('post_detail', slug=post.slug)

        elif 'reply_submit' in request.POST:
            reply_form = ReplyForm(request.POST)
            

            

            if reply_form.is_valid():
                comment_id = request.POST.get('comment_id')
                comment = get_object_or_404(Comment, pk=comment_id)
                reply = reply_form.save(commit=False)
                reply.comment = comment
                # reply.author = request.user
                # reply.author_email = request.user.email
                # reply.name = request.user.get_full_name
                reply.save()
                return redirect('post_detail', slug=post.slug)

    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
        'reply_form': reply_form,
        'comments': comments,
    })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            post.tags.set(form.cleaned_data['tags'])
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            post.tags.set(form.cleaned_data['tags'])
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def logout(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:

            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password.'})
def user_detail(request):
    user = get_object_or_404(User, pk=request.user.id)
    return render(request, 'registration/user_detail.html', context={"user":user})

def user_edit(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            
            user.save()
            return redirect('user_detail')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'registration/user_edit.html', {'form': form})



            