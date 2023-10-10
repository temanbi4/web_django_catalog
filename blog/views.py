from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from blog.models import BlogPost
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class BlogListView(ListView):
    model = BlogPost


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()

        return self.object

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'is_published')

    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blogpost_detail', args=[self.kwargs.get('slug')])



class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blogpost_list')

