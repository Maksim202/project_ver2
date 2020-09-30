from django.http import JsonResponse
from django.shortcuts import render
from .models import Article, Image
from django.core.paginator import Paginator

def index(request):

    latest_atricles_list = Article.objects.order_by('-pub_date')
    paginator = Paginator(latest_atricles_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number,)
    return render(request, 'home/list.html', {'latest_atricles_list': latest_atricles_list,'page_obj': page_obj})



def detail(request, home_id):
    a = Article.objects.get(id=home_id)
    images = Image.objects.filter(article=a)
    return render(request, 'home/detail.html',  {'a': a, 'images': images})


