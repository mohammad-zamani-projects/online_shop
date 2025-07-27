from django import template

from blog.models import Post

register = template.Library()


@register.simple_tag
def get_posts():
    return Post.objects.all()


# @register.simple_tag()
# def get_posts_image():
#     return Post.objects.

