from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item,Purchase

def greetings(request, item_id):
    return HttpResponse(f'Вы находитесь на странице для просмотра товара {item_id} ')

def list_item(request,):
    items = Item.objects.all()
    context = {
            'items': items,
        }
    return render(request,'list_item.html', context)

def detail_item(request, item_id):
    item = Item.objects.filter(id=item_id)
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
    }
    return render(request, 'detail_item.html', context)



