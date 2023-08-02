from django.shortcuts import render

from posts.models import Post


def index(request):
    context = {
        "title": "JOPA",
        "posts": Post.objects.all()
    }
    return render(request, "index.html",context=context)
