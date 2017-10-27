# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

# Views for groups
from ..models.groups import Group


def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    else:
        groups = groups.order_by('title')

    # apply pagination, 2 groups per page
    # context = paginate(groups, 2, request, {}, var_name='groups')

    return render(request, 'students/groups_list.html',  {'groups': groups})

def groups_add(request):
      return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
      return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
      return HttpResponse('<h1>Delete Group %s</h1>' % gid)