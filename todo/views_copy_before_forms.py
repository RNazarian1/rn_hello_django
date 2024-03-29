""".git/Docstring
"""
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.


def get_todo_list(request):
    """
    # return HttpResponse("Hello")
    """
    items = Item.objects.all()
    context = {
        'items': items
    }

    return render(request, './todo/todo_list.html', context)


def add_item(request):
    """
    # return HttpResponse("Hello")
    """
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, './todo/add_item.html')
