from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    return render(request, template_name= 'ToDoApp/index.html')

@csrf_exempt
def add_todo(request):
    print (request)
    return render(request, template_name= 'ToDoApp/index.html')
