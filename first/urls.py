# from django.urls import re_path, path
# # from . import views
# from first.views import index


# urlpatterns = [
#     # re_path(r'^$', index, name='index'),
#      path('', index),

# ]
from django.urls import path

from first.views import index


urlpatterns = [
    path('', index),
]