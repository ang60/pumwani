from django import template

register = template.Library()

@register.simple_tag
def payment():
    payment_methods = [
        'NHIF',
        'Linda mama',
        'Other insurances',
    ]

    return payment_methods
