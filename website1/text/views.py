from django.views import generic
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Log, Entry
from .forms import UserForm, LogForm, EntryForm
import datetime

now = datetime.datetime.now()

class IndexView(generic.ListView):
    template_name = 'text/index.html'
    context_object_name = 'all_logs'

    def get_queryset(self):
        return Log.objects.all()

class DetailView(generic.DeleteView):
    model = Log
    template_name = 'text/detail.html'

def create_log(request):
    if not request.user.is_authenticated():
        return render(request, 'text/login.html')
    else:
        form = LogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.date = now
            log.save()
            return render(request, 'text/detail.html', {'log': log})
        context = {
            "form": form,
        }
        return render(request, 'text/log_form.html', context)


def create_entry(request, log_id):
    form = EntryForm(request.POST or None, request.FILES or None)
    log = get_object_or_404(Log, pk=log_id)
    if form.is_valid():
        logs_entries = log.entry_set.all()
        for s in logs_entries:
            if s.title == form.cleaned_data.get("entry_title"):
                context = {
                    'log': log,
                    'form': form,
                    'error_message': 'You already added that entry',
                }
                return render(request, 'text/create_entry.html', context)
        entry = form.save(commit=False)
        entry.log = log
        context = {'log':log}
        return render(request, 'text/create_entry.html', context)
        entry.save()
        return render(request, 'text/detail.html', {'log': log})
    context = {
        'log': log,
        'form': form,
    }
    return render(request, 'text/create_entry.html', context)


class EntryCreate(CreateView):
    model = Entry
    fields = ['log', 'title', 'date', 'text']

class LogUpdate(UpdateView):
    model = Log
    fields = ['title', 'category', 'date']

class LogDelete(DeleteView):
    model = Log
    success_url = reverse_lazy('text:index')


class UserFormCreate(View):
    form_class = UserForm
    template_name = 'text/registration-form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('text:index')

        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                logs = Log.objects.filter(user=request.user)
                return render(request, 'text/index.html', {'logs': logs})
            else:
                return render(request, 'text/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'text/login.html', {'error_message': 'Invalid login'})
    return render(request, 'text/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'text/login.html', context)
