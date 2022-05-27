from django import views
from django.test import TestCase
from django.urls import resolve, reverse
from .views import *

# Create your tests here.

class BlogURLsTest(TestCase):
    def test_post_search_url_is_correct(self):
        url = reverse('blog:search', kwargs={'id':1})
        self.assertEqual(url, '/blog/search/')


class BlogViewsTest(TestCase):
    def test_blog_search_uses_correct_view_function(self):
        #url = reverse('blog:search', kwargs={'id':1})
        resolved = resolve(reverse('blog:search'))
        self.assertIs(resolved.func, views.search)