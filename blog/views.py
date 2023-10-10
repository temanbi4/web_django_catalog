from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy
from .forms import BlogPostForm

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        # Получаем объект записи блога
        post = super().get_object(queryset=queryset)
        # Увеличиваем счетчик просмотров на 1
        post.views_count += 1
        post.save()
        return post

class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm  # Используйте вашу форму BlogPostForm
    template_name = 'blog/blog_post_form.html'
    success_url = reverse_lazy('blog:blog_post_list')  # Укажите URL для перенаправления после успешного создания

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/blog_post_form.html'

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_post_list')

def blog_post_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    form = BlogPostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('blog:blog_post_list')

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'blog/blog_post_list.html', context)