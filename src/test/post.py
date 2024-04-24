# blog.py
class Post:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_posts(self):
        return self.posts
