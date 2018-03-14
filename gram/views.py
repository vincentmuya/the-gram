from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewPostForm,ProfileForms,CommentForm
from .models import Post,Profile,Comments
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    gram = Post.this_post()
    insta = Profile.this_profile()
    comment = Comments.this_comment()
    return render(request, "index.html", {"gram":gram, "insta":insta, "comment":comment})

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

def profile(request):
    return render(request,'all-scoots/index.html')

def profile(request):
    user = request.user
    gram = Profile.this_profile()
    image= Post.this_post()
    return render(request, "profile.html", {"gram":gram,
                                            "user":user,
                                            "image":image,})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

    else:
        form = ProfileForms()
    return render(request, 'edit_profile.html', {"form": form},)

def comment(request):
    return render(request, 'index.html')
