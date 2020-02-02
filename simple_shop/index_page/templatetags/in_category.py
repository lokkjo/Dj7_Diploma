from django import template

register = template.Library()

@register.filter
def in_category(things, category):
    return things.filter(type_id=category).order_by('-add_time')[:3]