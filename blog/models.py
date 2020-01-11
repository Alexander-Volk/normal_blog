from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField(blank=True, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
