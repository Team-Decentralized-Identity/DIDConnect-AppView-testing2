# test for posts
import unittest
from post import Post
import pytest

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog = Post()

    def test_add_post(self):
        self.blog.add_post("Hello, world!")
        self.assertEqual(self.blog.get_posts(), ["Hello, world!"])

    def test_empty_on_initialization(self):
        self.assertEqual(self.blog.get_posts(), [])

    def test_multiple_posts(self):
        posts = ["Hello, world!", "Another post", "Third post"]
        for post in posts:
            self.blog.add_post(post)
        self.assertEqual(self.blog.get_posts(), posts)

if __name__ == "__main__":
    unittest.main()