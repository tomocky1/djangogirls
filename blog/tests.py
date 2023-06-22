from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
# Create your tests here.

class PostTestCase(TestCase):
    def test_posts_get(self):
        Post.objects.create(author=get_user_model(),title="タイトル1",text="本文1")
        post = Post.objects.get(title="タイトル1")
        self.assertEqual(post.title, "タイトル1")