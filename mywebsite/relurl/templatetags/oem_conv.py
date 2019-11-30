from django import template

register = template.Library()

@register.filter(name='oem')
def oem_conv(inp,  to_name):
    return inp.replace(to_name, 'Lenevo')