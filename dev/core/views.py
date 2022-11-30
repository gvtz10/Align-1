from django.shortcuts import render, redirect
from django.views import View

from .forms import NewUserForm, ProjectForm, ActionForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from .models import Project, Action, File


# Create your views here.
def user_signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful!")
            return redirect(f'../home')
    form = NewUserForm()
    context = {
        'signup_form': form,
        }
    return render(request, 'core/user_signup.html', context)


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            fdata = form.cleaned_data
            username = fdata.get('username')
            password = fdata.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logged in as {username}")
                return redirect(f'../home')
            else:
                messages.error(request, "Invaids username or password")
        messages.error(request, "Invaids username or password")
    form = AuthenticationForm()
    context = {
        'login_form': form,
        }
    return render(request, 'core/user_login.html', context)


class HomeView(View):
    template_name = 'core/home_list.html'

    def get(self, request, *args, **kwargs):
        print("Get Home View!")
        print(request.GET)
        user = request.user
        proj_set = user.project_set.all()
        print(proj_set)
        context = {
            'user': user,
            'proj_set': proj_set,
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            }
        return render(request, self.template_name, context)


class ProjectView(View):
    template_name = 'core/proj_detail.html'

    def get(self, request, *args, **kwargs):
        print("Get Project View!")
        print(request.GET)
        user = request.user
        # proj_set = User.objects.get(id=user.id).project_set.all()
        proj_form = ProjectForm()
        context = {
            'user': user,
            'proj_form': proj_form,
            # 'proj_set': proj_set,
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


class ActionView(View):
    template_name = 'core/act_list.html'

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

