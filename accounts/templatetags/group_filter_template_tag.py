from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, groups_names):
    groups_collection = []
    groups_lst = groups_names.split(', ')
    for item in groups_lst:
        group = Group.objects.get(name=item)
        groups_collection.append(group)

    result = [x for x in groups_collection if x in user.groups.all()]
    return True if result else False


# def has_group(user, group_name):
#     group = Group.objects.get(name=group_name)
#     return True if group in user.groups.all() else False
