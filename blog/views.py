from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost 
from .forms import BlogPostForm

def post_list(request):
    posts = BlogPost.objects.all()    
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_create(request):  
    if request.method == "POST":        
        form = BlogPostForm(request.POST)     
        if form.is_valid():        
            form.save()           
            return redirect('post_list')   
    else:      
        form = BlogPostForm()    
        return render(request, 'blog/post_form.html', {'form': form})
    

def post_update(request, pk):    
    post = get_object_or_404(BlogPost, pk=pk)    
    if request.method == "POST":        
        form = BlogPostForm(request.POST, instance=post)        
        if form.is_valid():            
            form.save()            
            return 
        redirect('post_list')    
    else:        
        form = BlogPostForm(instance=post)    
    return render(request, 'blog/post_form.html', {'form': form})
    
    
def post_delete(request, pk):    
    post = get_object_or_404(BlogPost, pk=pk)    
    if request.method == "POST":        
        post.delete()        
        return redirect('post_list')    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})