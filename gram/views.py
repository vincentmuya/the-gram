from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewPostForm,ProfileForm,CommentForm,UserForm
from .models import Post,Profile,Comments
from django.contrib.auth.models import User
from django.db import transaction

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    gram = Post.this_post()
    comment = Comments.this_comment()
    return render(request, "index.html", {"gram":gram, "comment":comment})

def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form})

@login_required(login_url='/accounts/login')
def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExit:
        raise Http404()
    return render(request,"post.html", {"post":post})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form},)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def comment(request):
    return render(request, 'index.html')
