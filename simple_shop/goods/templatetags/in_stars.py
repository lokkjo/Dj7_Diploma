from django import template

register = template.Library()

@register.filter
def in_stars(integer):
    star = '★'
    return star * int(integer)