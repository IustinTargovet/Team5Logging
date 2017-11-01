from django.views import generic
from .models import Log

class IndexView(generic.ListView):
    template_name = 'text/index.html'
    context_object_name = 'all_logs'

    def get_queryset(self):
        return Log.objects.all()

class DetailView(generic.DeleteView):
    model = Log
    template_name = 'text/detail.html'
