from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    from menu_app.models import MenuItem
    menu_items = MenuItem.objects.filter(parent__isnull=True, name=menu_name).select_related('parent').prefetch_related('children')
    return render_to_string('menu.html', {'menu_items': menu_items})
