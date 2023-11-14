from django import template
from show_info.models import *

register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.all()
