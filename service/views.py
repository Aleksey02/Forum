from django.shortcuts import render, redirect
from service.models import Post, Coment
from django.views.generic import  ListView, DetailView, CreateView, DeleteView, UpdateView
from .form import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required #для функции
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  #для класса

def index(request):
    return render(request, 'index.html')

# @user_passes_test('test_func')
def about(request):
    return render(request, 'about.html')

# def test_func(user):
#     return user.email.endswith('@example.com')

# class MyView(UserPassesTestMixin, View):
#     def test_func(self):
#         return self.request.user.email.endswith('@example.com')

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

# class UsePerm(PermissionRequiredMixin):
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs) можно погуглить

class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_post'
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    #fields = "__all__"

class DeletePostView(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_post'
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class UpdatePostView(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_post'
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Coment
    template_name = 'add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

