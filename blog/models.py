from django.conf import settings
from django.db import models
from django.utils import timezone

# Code to handle posting a new blog
class Post(models.Model):
    # define what we expect for each property
    # Because we didn't specify a primary key in our Post model, Django
    #   creates one for us (by default, a number that increases by one
    #   for each record, i.e. 1, 2, 3) and adds it as a field named pk
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title