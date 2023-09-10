from .models import TodoListItem
from django.http import HttpResponseRedirect


def add_item(request):
    text = request.POST.get("content")
    new_item = TodoListItem(content=text)
    new_item.save()
    return HttpResponseRedirect(redirect_to="/todo/")


def delete_item(request, item):
    obj = TodoListItem.objects.get(pk=item)
    obj.delete()
    return HttpResponseRedirect(redirect_to="/todo/")
