from django.forms import BooleanField
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
import time
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post
# @login_required(login_url='login')
from rest_framework import viewsets
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .mixins import LikedMixin
from django.contrib.auth.models import User
from .serializers import UserSerializer


@login_required(login_url='login')
def post_list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'post_list.html', {'posts': posts})


def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_delete(request, pk):
    post_to_delete = get_object_or_404(Post, pk=pk)
    post_to_delete.delete()
    return HttpResponseRedirect()


class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', 'admin/')
        return HttpResponseRedirect(next)

    from .models import Post


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import authentication, permissions


# class AddLikeAPI(APIView):
#
#     authentication_classes = (authentication.SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#
#
#     def get(self, request, slug=None, format=None):
#         post = Post.objects.get()
#         # slug = self.kwargs.get("slug")
#         obj = get_object_or_404(Post, slug=slug)
#         url_ = obj.get_absolute_url()
#         user = self.request.user
#         updated = False
#         liked = False
#         if user.is_authenticated():
#             # if user in post.dislikes.all():
#             #     liked = False
#             #     post.likes.remove(user)
#             for like in post.likes.all():
#                 if like == request.user:
#                     is_like = False
#                     print("OK")
#
#             else:
#                 liked = True
#                 post.likes.add(request.user)
#         data = {
#             # "updated": updated,
#             "liked": liked
#         }
#         return Response(data)


# class PostViewSet(LikedMixin,
#                    viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)


class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', 'admin/')
        return HttpResponseRedirect(next)


class UserList(APIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    # return Response({"users": serializer.data})
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})


# def get(self, request, slug=None, format=None):
#         post = Post.objects.get()
#         # slug = self.kwargs.get("slug")
#         obj = get_object_or_404(Post, slug=slug)
#         url_ = obj.get_absolute_url()
#         user = self.request.user
#         updated = False
#         liked = False
#         if user.is_authenticated():
#             # if user in post.dislikes.all():
#             #     liked = False
#             #     post.likes.remove(user)
#             for like in post.likes.all():
#                 if like == request.user:
#                     is_like = False
#                     print("OK")
#
#             else:
#                 liked = True
#                 post.likes.add(request.user)
#         data = {
#             # "updated": updated,
#             "liked": liked
#         }
#         return Response(data)

class UserDetail(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
