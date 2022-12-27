from django import template

register = template.Library()


@register.filter
def do_capitals(value):
    return value.capitalize()
