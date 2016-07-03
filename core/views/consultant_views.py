from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.models import Consultant

class ConsultantList(ListView):
    model = Consultant

class ConsultantCreate(CreateView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
    fields = ['consultant_name', 'consultant_CRM',]

class ConsultantUpdate(UpdateView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
    fields = ['consultant_name', 'consultant_CRM',]

class ConsultantDelete(DeleteView):
    model = Consultant
    success_url = reverse_lazy('consultant_list')
