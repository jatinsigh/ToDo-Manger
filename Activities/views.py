from django.shortcuts import render,get_object_or_404
from .models import task as tk
from django.contrib.auth.models import User
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

context={
    'tk':tk.objects.all()
}

def home(request):
    return render(request,'Activities/home.html')

def about(request):
    return render(request,'Activities/about.html')

@method_decorator(login_required, name='dispatch')
class UserPostListView(ListView):
    model=tk
    template_name='Activities/user_task.html'
    context_object_name = 'tk'

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return tk.objects.filter(author=user)

"""
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = tk
    fields=['content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
"""
class PostDetailedView(DetailView):
    model = tk

class PostDeleteView(DeleteView):
    model = tk
    success_url='/'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = tk
    fields=['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
