from django.shortcuts import render, redirect
from service.models import Post, Coment
from django.views.generic import  ListView, DetailView, CreateView, DeleteView, UpdateView
from .form import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class PostsView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']

class DetailPostView(DetailView):
    model = Post
    template_name = 'detail_post.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    #fields = "__all__"

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm

class AddCommentView(CreateView):
    model = Coment
    template_name = 'add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
