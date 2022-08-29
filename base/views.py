from django.shortcuts import render,redirect

from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.urls import reverse_lazy

from base.forms import TaskForm, UserCreateForm 
from .models import Tast

# Login view
class BaseLoginView(LoginView):
	template_name = 'base/login.html'
	fields = '__all__'
	redirect_authenticated_user = True
    
    # Redirect user to view dashboard
	def get_success_url(self):
		return reverse_lazy('tasks')


class RegisterView(FormView):
	form_class = UserCreateForm
	template_name = 'base/register.html'
	success_url = reverse_lazy('tasks')
	context_object_name = 'form'

	# Redirect user and make sure user is loggedin
	def form_valid(self, form):
		user = form.save()

		if user :
			reverse_lazy('tasks')

		return super(RegisterView, self).form_valid(form)

	def get(self, *args, **kwargs):
		# Authenticated users cannot view the regster page after being authenticated
		if self.request.user.is_authenticated :
			return redirect('tasks')
			
		return super(RegisterView, self).get(self, *args, **kwargs)

# Logout
class BaseLogoutView(LogoutView):
	next_page = 'login-user'

# Class view to view a list of objects
class TaskList(LoginRequiredMixin, ListView):
	model = Tast
	template_name = 'base/index.html'
	context_object_name = 'tasks'
	paginate_by = 7

	def get_queryset(self):
		return Tast.objects.filter(user=self.request.user)

# View to view details of an object
class TaskDetail(LoginRequiredMixin, DetailView):
	model = Tast
	template_name = 'base/taskdetail.html'
	context_object_name = 'task'
	pk_url_kwarg = 'id'

class TaskCreate(LoginRequiredMixin, CreateView):
	model = Tast
	template_name = 'base/create-task.html'
	form_class = TaskForm
	success_url = reverse_lazy('tasks')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
	model = Tast
	template_name = 'base/task-update.html'
	success_url = reverse_lazy('tasks')
	form_class = TaskForm
	pk_url_kwarg = 'id'

	def form_valid(self, form):
		form.instance.user = self.request.user

		return super(TaskUpdate, self).form_valid(form)


class TaskDelete(LoginRequiredMixin, DeleteView):
	model = Tast
	template_name = 'base/delete-task.html'
	context_object_name = 'taskdelete'
	success_url = reverse_lazy('tasks')
	pk_url_kwarg = 'id'

	def form_valid(self, form):
		form.instance.user = self.request.user

		return super(TaskDelete, self).form_valid(form)