from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import PostForm, UserRegisterForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES) # para acceder a la info enviada atraves de esta form
        if form.is_valid(): #Verifica que la form se haya llenado correctamente
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {'form': form }
    return render(request, 'social/register.html', context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post publicado!')
            return redirect('feed')
    else:
        form = PostForm()
    context = {'form': form }
    return render(request, 'social/post.html', context)

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        user = request.user
        posts = current_user.posts.all()
    context = {'user': user, 'posts': posts}
    return render(request, 'social/profile.html', context)


def follow(request, username):
    current_user = request.user #Usuario logueado
    to_user = User.objects.get(username=username)
    rel = Relationship(from_user=current_user, to_user=to_user)
    rel.save()
    messages.success(request, f'sigues a {username}!')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user #Usuario logueado
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'ya no sigues a {username}!')
    return redirect('feed')