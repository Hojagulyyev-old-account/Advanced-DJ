from django import template

register = template.Library()

@register.simple_tag
def change_language(*args, **kwargs):
    redirect = f"/{kwargs['lang']}{kwargs['path']}"
    if kwargs['path'].startswith('/en/') or kwargs['path'].startswith('/tk/'):
        redirect = f"/{kwargs['lang']}/{kwargs['path'][4:]}"
        
    return redirect
