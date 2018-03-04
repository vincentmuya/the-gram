from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    return render(request, "index.html")

@login_required(login_url='/new/post')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()

        else:
            form = NewPostForm()
        return render(request, 'new_post.html', {"form": form},)
