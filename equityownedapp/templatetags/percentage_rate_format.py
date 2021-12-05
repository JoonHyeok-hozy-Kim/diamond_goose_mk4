from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

def percentage_rate_format(amount):
    amount = round(float(amount*100), 2)
    result = "%s%s" % (intcomma(int(amount)), ("%0.2f" % amount)[-3:])
    result += '%'
    return result

register.filter('percentage_rate_format', percentage_rate_format)
register.filter('intcomma', intcomma)