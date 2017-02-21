from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blog.models import BlogPost, Comment, User
from django import forms
import time
import datetime
from forms import CommentForm


# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(label='confirm password',
                                widget=forms.PasswordInput())


class UserFormLogin(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def login(request):
    if request.method == "POST":
        uf = UserFormLogin(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = User.objects.filter(username=username,
                                             password=password)
            if (len(userResult) > 0):
                return HttpResponseRedirect("blog-list")
            else:
                pass
    else:
        uf = UserFormLogin()
    return render_to_response('login.html', {'uf': uf})


def register(request):
    curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            filterResult = User.objects.filter(username=username)
            if len(filterResult) > 0:
                return render_to_response('register.html',
                                    {"errors": "username already exists"})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                errors = []
            if (password2 != password1):
                errors.append("Two passwords are inconsistent")
                return render_to_response('register.html', {'errors': errors})
            password = password2
            user = User.objects.create(username=username, password=password1)
            user.save()
            return render_to_response('success.html')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf})


def get_blogs(request):
    ctx = {
        'blogs': BlogPost.objects.all().order_by('-timestamp')
    }
    return render(request, 'blog-list.html', ctx)


def get_detail(request, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html', ctx)
