from django.shortcuts import render, get_object_or_404
from .models import Category, Item

def index(request):
    items = Item.objects.all()
    return render(request, 'cmsapp/index.html', {'items': items})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = category.item_set.all()
    return render(request, 'cmsapp/category_detail.html', {'category': category, 'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'cmsapp/item_detail.html', {'item': item})

def search(request):
    query = request.GET.get('q')
    filter_by = request.GET.get('filter_by')
    if filter_by == 'title':
        results = Item.objects.filter(title__icontains=query)
    elif filter_by == 'date':
        results = Item.objects.filter(pub_date__date=query)
    elif filter_by == 'category':
        results = Item.objects.filter(category__name__icontains=query)
    else:
        results = Item.objects.all()
        
    return render(request, 'cmsapp/search_results.html', {'results': results})