from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tast

class TaskForm(ModelForm):
	class Meta:
		model = Tast
		fields = ['title', 'description', 'complete']

class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'form-control'})