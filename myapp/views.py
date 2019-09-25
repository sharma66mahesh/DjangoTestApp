from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView

# Create your views here.

class IndexView(ListView):
    template_name = "myapp/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return Post.objects.all()



