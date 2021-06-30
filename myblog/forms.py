from django import forms
from django.contrib.auth import models
from django import forms
from .models import Comment, Post, Category

# choices = [('coding', 'coding'), ('sports', 'sports'), ('gaming', 'gaming')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm): # Назначали поля в виде виджетов для вкладки Add Post, присваивали класс CSS из Bootstrap
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}) убрал поле, чтобы проект сам понимал после LogIn, кто делает пост,
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm): # Назначали поля в виде виджетов для вкладки Add Post, присваивали класс CSS из Bootstrap
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}), 
            # 'author': forms.Select(attrs={'class': 'form-control'}), Убираем лишнее поле для Update post
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class CommentForm(forms.ModelForm): # Назначали поля в виде виджетов для вкладки Add Post, присваивали класс CSS из Bootstrap
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    