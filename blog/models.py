from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
