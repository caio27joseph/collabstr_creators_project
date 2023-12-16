from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_host(context):
    request = context["request"]
    return request.get_host()
