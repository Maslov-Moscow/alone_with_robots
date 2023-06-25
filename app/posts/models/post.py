from django.db import models

from posts.querysets import PostQuerySet


class Post(models.Model):
    objects = PostQuerySet.as_manager()

    author = models.ForeignKey(
        verbose_name="Author", to="users.User", on_delete=models.CASCADE
    )
    text = models.TextField("Text")
    pub_date = models.DateTimeField("Publish date", auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
