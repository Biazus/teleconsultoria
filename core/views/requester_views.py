from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.models import Requester

class RequesterList(ListView):
    model = Requester

class RequesterCreate(CreateView):
    model = Requester
    success_url = reverse_lazy('requester_list')
    fields = ['requester_name', 'requester_email', 'requester_phone']

class RequesterUpdate(UpdateView):
    model = Requester
    success_url = reverse_lazy('requester_list')
    fields = ['requester_name', 'requester_email', 'requester_phone']

class RequesterDelete(DeleteView):
    model = Requester
    success_url = reverse_lazy('requester_list')
