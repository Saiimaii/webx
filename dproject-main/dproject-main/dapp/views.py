from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_ro_404, render
from .models import Todo

def index(request):
	return render(request, 'index.html')

def update_content(request):
	return HttpResponse('<div>hello from HTMX</div>')

def update_content2(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        return render(request, 'partial_content.html', {'data': data})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        new_todo = Todo.objects.create(title=title)
        return render(request, 'todo_item.html', {'todo' : new_todo})
    
def delete_todo(request, todo_id):
    todo = get_object_ro_404(Todo, id=todo_id)
    todo.delete()
    return HttpResponse(status=200)

def taggle_todo(request, todo_id):
    todo = get_object_ro_404(Todo, id=todo_id)
    todo.comleted = not todo.comleted
    todo.save()
    return render(request, 'todo_item.html', {'todo' : todo})

def edit_todo(request, todo_id):
    if request.method == 'POST':
        todo = get_object_ro_404(Todo, id=todo_id)
        todo.title = request.POST.get('title')
        todo.save()
        return render(request, 'todo_item.html', {'todo' : todo})
    
def edit_todo_form(request, todo_id):
    todo = get_object_ro_404(Todo, id=todo_id)
    title = todo.title
    return render(request, 'todo_item_form.html', {'todo' : todo, 'title' : title})

def cancle_edit(request, todo_id):
    todo = get_object_ro_404(Todo, id=todo_id)
    return render(request, 'todo_item.html', {'todo' : todo})
    
