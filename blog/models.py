from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField(blank=True, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
