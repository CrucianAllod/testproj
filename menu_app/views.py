from django.shortcuts import render
from .models import MenuItem

def menu_view(request, name):
    menu_items = MenuItem.objects.filter(parent__isnull=True).select_related('parent').prefetch_related('children')
    return render(request, 'menu.html', {'menu_items': menu_items})