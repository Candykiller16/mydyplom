from django.urls.base import reverse
from myblog.models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Category, Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True 

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' ')) #замена пробела на - при именновании категории
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context



class AddPostView(CreateView):
    model = Post   
    form_class = PostForm   # Присваивали таблице форму с полями для заполнения из forms.py в Add Post вкладке
    template_name = 'add_post.html'
    # fields = '__all__'
    # # fields = ('title', 'body')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm   
    template_name = 'add_comments.html'

    def form_valid(self, form):
	    form.instance.post_id = self.kwargs['pk']
	    return super().form_valid(form)

    success_url = reverse_lazy('home')




class AddCategoryView(CreateView):
    model = Category   
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # # fields = ('title', 'body')    


class UpdatePostView(UpdateView):
    model = Post  
    form_class = EditForm 
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body'] form_class не работает вместе с fields


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')