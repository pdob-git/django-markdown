import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown.extensions import codehilite

register = template.Library()

@register.filter
@stringfilter
def render_markdown(value):
    md = markdown.Markdown(extensions=["fenced_code","codehilite"])
    value = value.replace('\\' + '\r\n', '<br/>')
    return mark_safe(md.convert(value))


