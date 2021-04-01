from django.views.generic import DetailView, ListView

from .models import Post

class PostListView(ListView): # Criei as classes para herdarem as views e depois crei a variavel model" para receberem o valor de Post(classe criada em models.py) , ou seja os posts
    model = Post
    paginate_by = 10
    
    
class PostDetailView(DetailView):
    model = Post

# Create your views here.
