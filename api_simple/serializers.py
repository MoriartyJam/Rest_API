from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post

from . import views
from django.contrib.auth.models import User


# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['author', 'pub_date', 'likes']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['owner', 'title', 'pub_date', 'likes']

    def get_full_name(self, obj):
        return obj.get_full_name()

    # def get_is_fan(self, obj) -> bool:
    #
    #     user = self.context.get('request').user
    #     return likes_services.is_fan(obj, user)


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']
