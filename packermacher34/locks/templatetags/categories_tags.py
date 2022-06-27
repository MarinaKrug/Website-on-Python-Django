from django import template

from locks.models import Category

register = template.Library()




@register.inclusion_tag('locks/list_category.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.simple_tag(name='get_cats')
def get_cats():
    return Category.objects.all()