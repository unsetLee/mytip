from django.shortcuts import render

# Create your views here.

def content_list(request):
    return render(request, 'content/content_list.html')