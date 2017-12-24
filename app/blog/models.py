from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(
        "authentication.Member", on_delete=models.CASCADE,
        related_name="blogs"
    )
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __unicode__(self):
        return self.title
