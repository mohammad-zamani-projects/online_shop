from django.urls import path, register_converter, re_path
from blog.views import view1, show_year, show_name, view3
from blog.utils import FourDigitYear

register_converter(FourDigitYear, "four_digit")

urlpatterns = [
    path('list/', view1),
    # path('year/<four_digit:input_year>', show_year),
    re_path(r'year/(?P<input_year>[0-9]{2,4})/', show_year),
    path('name/<str:input_name>/', show_name),
    path('categories/list', view3),
]
