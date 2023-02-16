from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split_str(str):
    """Splits a path, that is a string and returns the last item, which is the name of the file."""
    final_str = str.split("/")[-1]
    return final_str


@register.filter
@stringfilter
def remove_prefix(input_string):
    prefix = str(settings.BASE_DIR)
    if prefix and input_string.startswith(prefix):
        return input_string[len(prefix) :]
    return input_string
