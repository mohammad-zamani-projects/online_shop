from django.urls import path
from blog.views import test1, test2, test3


urlpatterns = [
    path('list/', test1),
    path('detail/hello_world', test2),
    path('categories/list', test3),
]
