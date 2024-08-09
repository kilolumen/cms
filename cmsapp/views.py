from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Category, Item

def index(request):
    items = Item.objects.all().order_by('-pub_date')
    paginator = Paginator(items, 5)  # Show 5 items per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'items': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'cms/index.html', context)

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cmsapp/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'cmsapp/item_form.html', {'form': form})

@login_required
def item_update(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('index_detail', item_id=item.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'cmsapp/item_form.html', {'form': form})

@login_required
def item_delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    else:
        return render(request, 'cmsapp/item_confirm_delete.html', {'item': item})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'cms/item_list.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'cms/item_detail.html', {'item': item})
