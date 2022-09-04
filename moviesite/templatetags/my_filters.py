from django import template

register = template.Library()


@register.filter
def my_range(value, inter):
    return range(value-inter, value+inter+1)
