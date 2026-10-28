from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # password = models.CharField(max_length=10)


class Post(models.Model):
    title = models.CharField(max_length=100)
    main_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
