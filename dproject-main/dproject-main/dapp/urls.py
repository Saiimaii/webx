from .views import add_todo, cancle_edit, delete_todo, edit_todo, edit_todo_form, index, taggle_todo, updete_content
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='index'),
	path('update/', updete_content, name='update_content'),
 	path('update2/', updete_content, name='update_content2'),
	path('add/', add_todo, name='add_todo'),
 	path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
	path('toggle/<int:todo_id>/', taggle_todo, name='toggle_todo'), 
	path('edit/<int:todo_id>/', edit_todo, name='edit_todo'),
	path('edit_form/<int:todo_id>/', edit_todo_form, name='edit_todo_form'),
	path('cancle/<int:todo_id>/', cancle_edit, name='cancel_edit'),

 
 
 
]
