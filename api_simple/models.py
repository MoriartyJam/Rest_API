from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
# from django.core.urlresolvers import reverse
from django.urls import reverse


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, default=1, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='snippets', default=1,  on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # highlighted = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_like')
    dislikes = models.ManyToManyField(User, blank=True, related_name='post_dislike')


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_api_like_url(self):
        return reverse("posts:add_like_api", kwargs={"slug": self.slug})

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                               full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Snippet, self).save(*args, **kwargs)