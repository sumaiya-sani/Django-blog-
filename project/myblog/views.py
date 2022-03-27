from dataclasses import field
from pyexpat import model
from re import template

from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from.models import Category_path, Comment, Post
from.forms import  PostForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


#def home(request):  
 #   return render(request,'homepage.html',{})

def LikeView(request,pk):
    #TO BRING AN ID 
 
    post=Post.objects.get(id=pk)
     
    like_button=Post.objects.filter(likes=request.user) 
  
    if post in like_button:
      
     post.likes.remove(request.user)
   
    else: 
     
     post.likes.add(request.user) 
      
  
    return HttpResponseRedirect(reverse('myblog:article_detail',args=[str(pk)]),)




def categoryView(request,cats):
    category_post=Post.objects.filter(category_post=cats)
    return render(request,'categories.html',{'category_post':category_post})

class homeview(ListView):
     model=Post 
     template_name= 'homepage.html'
     ordering=['-date_of_post']

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_detail.html'

#comment section    
class AddCommentView(CreateView):
    model=Comment
    template_name='add_comment.html'
    #form_class= CommentForm
    fields=('name','body')
    success_url=reverse_lazy('myblog:article_detail')

#how to make the form valid for the specific post:
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)


#how to rrdirect to the same page that's the post in :
    def get_success_url(self, **kwargs):
        return reverse_lazy('myblog:article_detail', kwargs={'pk': self.kwargs['pk']})

#end comment section 

class AddPostView(CreateView):
    model=Post
    template_name='add_post.html'
    form_class=PostForm
    success_url=reverse_lazy('myblog:home')

class AddCategoryView(CreateView):
    model=Category_path
    template_name='add_category.html'
    fields='__all__'
    success_url=reverse_lazy('myblog:home')


    #fields='__all__'
class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    fields=['title','title_tag','snippets','body']
    success_url=reverse_lazy('myblog:home')

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('myblog:home')


