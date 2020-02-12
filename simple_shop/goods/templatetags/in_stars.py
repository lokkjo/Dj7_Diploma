from django import template

register = template.Library()
STAR = '★'


@register.filter
def in_stars(integer):
    return STAR * int(integer)