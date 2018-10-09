from django import template
from django.urls import reverse_lazy

register = template.Library()


@register.filter
def url_admin(instance, action):
    keys = ('history', 'delete', 'change', 'detail', 'changelist', 'add')
    with_pk = (instance.pk, ) if action in keys[:4] else None
    info = 'admin:%s_%s' % (instance._meta.app_label, instance._meta.model_name)
    actions = {k: '%s_%s' % (info, k) for k in keys}
    
    return reverse_lazy(actions[action], args=with_pk)
