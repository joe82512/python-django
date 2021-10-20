from django.shortcuts import render

# Create your views here.

# post
def post(request):
    return render(request, 'post.html')