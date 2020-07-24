from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . import models
from django.http import HttpResponseRedirect

def home_page(request):
    todo_items = models.ToDo.objects.all().order_by("pub_date")[::-1]
    return render(request, 'ToDoApp/index.html', {
        "todo_items" : todo_items,
    })

@csrf_exempt
def add_todo(request):
    # print (request.POST)
    added_date= timezone.now()
    content = request.POST["content"]
    create_obj=models.ToDo.objects.create( text = content, pub_date = added_date)
    length_of_todo = models.ToDo.objects.all().count()
    # print(length_of_todo)
    # print(create_obj)
    # print(create_obj.id) 
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    models.ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

