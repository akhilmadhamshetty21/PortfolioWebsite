from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Contact, Post
from django.views import generic


def index(request):
    return render(request, "mysite/index.html")


def portfolio(request):
    return render(request, "mysite/blogs.html")


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        c = Contact(email=email, name=name, message=message)
        c.save()

        return render(request, "mysite/contact.html")
    else:
        return render(request, "mysite/contact.html")


def category(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'mysite/categories.html', {'cats': cats, 'category_posts': category_posts})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'mysite/blogs.html'


def post_detail(request, slug):
    template_name = 'mysite/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
