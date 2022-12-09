# posts/test.py

from django.test import TestCase
from django.urls import reverse  #new

from .models import Post  # new

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text='this is a test!')
    
    # only this f(x) will run coz its prefixed with "test".
    def test_model_content(self):
        self.assertEqual(self.post.text, 'this is a test!')
    
    # now lets check our urls, views and templates
    
    def test_url_exist_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    '''
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'this is a test!')

    '''
    
    # combining the above three tests, because they all test one-
    # functionality that is the homepage
    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'this is a test!')
    