from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from api_simple.views import PostView, post_delete



urlpatterns = [
    url(r'^create/new/$', views.index, name='create'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/detail/$', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like', views.AddLike.as_view(), name='post_like'),
    # path('api/<int:pk>/', views.AddLikeAPI.as_view(), name='post_like_api'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('post/<int:pk>/dislike', views.AddDislike.as_view(), name='post_dislike'),
    url(r'post_list/', views.post_list, name="post_list"),
    # path('', include(router.urls, 'posts'), namespace='posts'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/(?P<slug>[\w-]+)/like/$', views.AddLikeAPI.as_view(), name='like-add-api'),
    path('posts/', PostView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),

]
