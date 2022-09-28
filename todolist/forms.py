from django.forms import ModelForm
from todolist.models import Task

# Create the form class.
class TaskForm(ModelForm):
     class Meta:
         model = Task
         fields = ['title', 'description']