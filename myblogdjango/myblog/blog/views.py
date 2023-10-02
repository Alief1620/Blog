from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm



class PostView(View):
    '''вывод записей'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})

        related_posts = Post.objects.filter(category=post.category).exclude(id=post.id).order_by('-published_date')[:10]


class AddComments(View):
    '''добавление комментария'''

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            post = Post.objects.get(id=pk)
            form.post_id = post
            form.save()
        return redirect(f'/{pk}')

