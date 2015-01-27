from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name="field_type")
def field_type(field):
    return field.__class__.__name__
